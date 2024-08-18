from currency_converter import CurrencyConverter
from config import API_KEY

def main():
    converter = CurrencyConverter(API_KEY)

    while True:
        print("\n--- Calculadora de Divisas ---")
        print("1. Convertir divisas")
        print("2. Salir")

        choice = input("Elige una opción: ")

        if choice == '1':
            from_currency = input("Divisa de origen (por ejemplo, USD): ").upper()
            to_currency = input("Divisa de destino (por ejemplo, EUR): ").upper()
            try:
                amount = float(input(f"Cantidad en {from_currency}: "))
                rate = converter.get_exchange_rate(from_currency, to_currency)
                if rate is not None:
                    converted_amount = amount * rate
                    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
                else:
                    print(f"No se pudo obtener la tasa de cambio para {from_currency} a {to_currency}.")
            except ValueError:
                print("Cantidad no válida. Intenta de nuevo.")
        elif choice == '2':
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

