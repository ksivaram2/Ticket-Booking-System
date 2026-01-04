from __future__ import annotations

class PricingService:
    def calculate_total(self, base_price: float, quantity: int) -> float:
        # Simple rule: quantity discount
        total = base_price * quantity
        if quantity >= 5:
            total *= 0.9
        return round(total, 2)
