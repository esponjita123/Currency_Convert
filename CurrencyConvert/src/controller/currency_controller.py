class CurrencyConverter:
    rates = {
        ('PEN', 'USD'): 0.26,
        ('USD', 'PEN'): 3.85,
        ('PEN', 'EUR'): 0.24,
        ('EUR', 'PEN'): 4.10,
        ('USD', 'EUR'): 0.92,
        ('EUR', 'USD'): 1.09,
    }

    @staticmethod
    def convert(amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency == to_currency:
            return amount
        key = (from_currency, to_currency)
        if key in CurrencyConverter.rates:
            return round(amount * CurrencyConverter.rates[key], 2)
        raise ValueError("Conversion rate not found!")
