import asyncio
import json


async def task2(names: list, prices: list):
    with open("task2.json", "r") as file:
        data = json.load(file)
        for i in range(len(names)):
            dict1 = {"name": names[i], "price": prices[i]}
            data["course"].append(dict1)

    with open("task2.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Task2 ga Task1 ma'lumotlari qo'shildi:")


async def task1():
    with open("task1.json", "r") as file:
        data = json.load(file)
        names = []
        prices = []
        for i in data["course"]:
            names.append(i["name"])
            prices.append(i["price"])
        print("Task2ga yuborildi:")
        await asyncio.gather(task2(names, prices))


async def main():
    await asyncio.gather(task1())


if __name__ == "__main__":
    asyncio.run(main())

# await ishlatilgan funksiyasini kutib turadi await qatoridagi kodlarni ishlatib olguncha
# run metodini oxirida qo'llash kk.
