# --- NIVEL 1 ---

# 1. Crea una clase que calcule estadísticas (count, sum, min, max, range, mean, median, 
# mode, standard_deviation, variance, frequency_distribution y describe).

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 != 0:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def mode(self):
        frecuencias = {}
        for item in self.data:
            frecuencias[item] = frecuencias.get(item, 0) + 1
            
        moda_valor = max(frecuencias, key=frecuencias.get)
        moda_cantidad = frecuencias[moda_valor]
        
        return {'mode': moda_valor, 'count': moda_cantidad}

    def variance(self):
        media = self.mean()
        varianza = sum((x - media) ** 2 for x in self.data) / self.count()
        return round(varianza, 1) 

    def standard_deviation(self):
        std_dev = self.variance() ** 0.5
        return round(std_dev, 1)

    def frequency_distribution(self):
        valores_unicos = sorted(set(self.data))
        return [(valor, self.data.count(valor)) for valor in valores_unicos]

    def describe(self):
        resumen = f"""
        Count: {self.count()}
        Sum:   {self.sum()}
        Min:   {self.min()}
        Max:   {self.max()}
        Range: {self.range()}
        Mean:  {self.mean()}
        Median:{self.median()}
        Mode:  {self.mode()}
        Var:   {self.variance()}
        Std:   {self.standard_deviation()}
        """
        return resumen


data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
statistics = Statistics(data)
print(statistics.describe())
# --- EJERCICIOS: NIVEL 2 ---

# 1. Crea una clase llamada 'PersonAccount'. 
# Debe tener firstname, lastname, incomes, expenses como atributos.
# Y métodos para añadir ingresos, añadir gastos y calcular el balance.
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
    
    def anadir_ingreso(self, cantidad, descripcion):
        self.incomes.append({"cantidad": cantidad, "descripcion": descripcion})
    
    def anadir_gasto(self, cantidad, descripcion):
        self.expenses.append({"cantidad": cantidad, "descripcion": descripcion})
    
    def total_income(self):
        return sum(item['amount'] for item in self.incomes)

    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)
    
    def banace(self):
        return self.incomes() - self.expenses()
        


# --- EJERCICIOS: NIVEL 3 ---

# 1. El siguiente código es una función; conviértelo en una clase con comportamiento equivalente:


def print_products(*args, **kwargs):
    for product in args:
        print(product)
    print(kwargs)
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

print_products("apple", "banana", "orange", vegetable="tomato", juice="orange")

class ProductPrinter:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print_products(self):
        for product in self.args:
            print(product)
            
        print(self.kwargs)
        
        for key, value in self.kwargs.items():
            print(f"{key}: {value}")

