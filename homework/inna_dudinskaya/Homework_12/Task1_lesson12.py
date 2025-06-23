class Flowers:
    def __init__(self, name, color, stem_length, freshness, price, time_of_life):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price
        self.time_of_life = time_of_life

    def __str__(self):
        return (f"{self.name} ({self.color}, стебель: {self.stem_length}см, свежесть: {self.freshness}дн,"
                f" цена: {self.price}руб, живет: {self.time_of_life}дн)")

    def __repr__(self):
        return (f"{self.name} ({self.color}, стебель: {self.stem_length}см, свежесть: {self.freshness}дн, "
                f"цена: {self.price}руб, живет: {self.time_of_life}дн)")


class Rose(Flowers):
    def __init__(self, color, stem_length, freshness, price, time_of_life=7):
        super().__init__("Роза", color, stem_length, freshness, price, time_of_life)


class Camomile(Flowers):
    def __init__(self, color, stem_length, freshness, price, time_of_life=10):
        super().__init__('Ромашка', color, stem_length, freshness, price, time_of_life)


class Tulip(Flowers):
    def __init__(self, color, stem_length, freshness, price, time_of_life=5):
        super().__init__('Тюльпан', color, stem_length, freshness, price, time_of_life)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_price(self):
        return sum(flower.price for flower in self.flowers)

    def count_flowers(self):
        return len(self.flowers)

    def average_time_of_life(self):
        return sum(flower.time_of_life for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def find_flowers_by_time_of_life(self, min_days, max_days):
        result = []
        for flower in self.flowers:
            if min_days <= flower.time_of_life <= max_days:
                result.append(flower)
        return result

    def __repr__(self):
        result = "\n"
        for flower in self.flowers:
            result += str(flower) + "\n"
        return result + f"Общая стоимость: {self.calculate_price()} руб"


rose_red = Rose("красный", 40, 2, 150)
rose_white = Rose("белый", 25, 1, 100)
camomile_white = Camomile("белый", 30, 1, 80)
tulip_red = Tulip("красный", 30, 3, 80)
tulip_yellow = Tulip("желтый", 35, 2, 90)

bouquet = Bouquet()
bouquet.add_flower(rose_red)
bouquet.add_flower(rose_white)
bouquet.add_flower(camomile_white)
bouquet.add_flower(tulip_red)
bouquet.add_flower(tulip_yellow)

print("Букет:")
print(bouquet)
print(f"\nСреднее время увядания букета: {bouquet.average_time_of_life():.1f} дней")

print("\nПоиск цветов, которые живут от 5 до 8 дней:")
for flower in bouquet.find_flowers_by_time_of_life(5, 8):
    print(flower)

print("\nСортировка по свежести:")
bouquet.sort_by_freshness()
print(bouquet)

print("\nСортировка по цвету:")
bouquet.sort_by_color()
print(bouquet)

print("\nСортировка по длине стебля:")
bouquet.sort_by_stem_length()
print(bouquet)

print("\nСортировка по стоимости:")
bouquet.sort_by_price()
print(bouquet)
