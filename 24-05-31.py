class Beverage:
    def __init__(self):
        self.menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}

    def 총가격계산(self, 음료이름, 수량):
        if 음료이름 in self.menu:
            가격 = self.menu[음료이름]
            총가격 = 가격 * 수량
            return 총가격
        else:
            return None

def main():
    음료 = Beverage()
    print("메뉴:")
    for 음료이름, 가격 in 음료.menu.items():
        print(f"{음료이름}: {가격} 원")

    음료이름 = input("메뉴를 선택해주세요: ")
    수량 = int(input("수량을 선택해주세요: "))

    총량 = 음료.총가격계산(음료이름, 수량)

    if 총량 is not None:
        print(f"{수량}개의 {음료이름}의 총 가격은 {총량} 원입니다.")
    else:
        print("메뉴에 없습니다.")

if __name__ == "__main__":
    main()
