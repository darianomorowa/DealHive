def calculate_active_discount(current_total, thresholds, discounts):
    active_discount = 0.0

    # hier gehen wir alle Preisstufen durch
    # leere Zeilen werden übersprungen, damit das Formular nicht crasht
    for i in range(len(thresholds)):
        if thresholds[i] and discounts[i]:
            threshold = int(thresholds[i])
            discount = float(discounts[i])

            # wenn die aktuelle Gesamtmenge die Stufe erreicht hat,
            # wird dieser Rabatt als aktiver Rabatt gespeichert
            if current_total >= threshold:
                active_discount = discount

    return active_discount


def active_discount_was_lowered(current_total, old_tiers, new_thresholds, new_discounts):
    old_thresholds = []
    old_discounts = []

    # hier wandeln wir die alten DB-Preisstaffeln in zwei Listen um
    # dadurch können wir die gleiche Berechnungsfunktion wiederverwenden
    for tier in old_tiers:
        old_thresholds.append(tier["threshold_quantity"])
        old_discounts.append(tier["discount_percent"])

    old_active_discount = calculate_active_discount(
        current_total,
        old_thresholds,
        old_discounts
    )

    new_active_discount = calculate_active_discount(
        current_total,
        new_thresholds,
        new_discounts
    )

    # wenn noch kein Rabatt aktiv war, darf der Creator die Staffeln frei bearbeiten
    if old_active_discount == 0:
        return False

    # sobald ein Rabatt aktiv war, darf der neue aktive Rabatt nicht kleiner sein
    return new_active_discount < old_active_discount