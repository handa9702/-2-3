from CompanyAddr import CompanyAddr
from CustomerAddr import CustomerAddr
from Address import Addr

class SmartPhone:
    def __init__(self):
        self.contacts = [] 

    def input_addr_data(self):
        name = input("이름:")  
        phone = input("전화번호:")
        email = input("이메일:")
        address = input("주소:")
        birthday = input("생일:")
        group = input("그룹:")
       
        if group == "회사":
             company = input("회사이름:")
             department = input("부서이름:")
             position = input("직급:")
             return CompanyAddr(name, phone, email , address, birthday, group, company, department, position)
    
        elif group == "거래처":
             customer = input("거래처이름:")
             item = input("품목이름:")
             position = input("직급:")
             return CustomerAddr(name, phone, email , address, birthday, group, customer, item, position)
        
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")

            
    def add_company_addr(self, company_addr):        
            self.contacts.append(company_addr)
            print(">>> 데이터가 저장되었습니다.")
    
    def add_customer_addr(self, customer_addr):       
            self.contacts.append(customer_addr)
            print(">>> 데이터가 저장되었습니다.")


    def print_all_addr(self):
        if not self.contacts:
            print("저장된 연락처가 없습니다.")
        else:
            for i, addr in enumerate(self.contacts):
                print(f"\n[{i+1}]")
                addr.print_info()

    def search_addr(self, name):
        for addr in self.contacts:
            if addr.get_name() == name:
                addr.print_info()
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")

    def delete_addr(self, name):
        for addr in self.contacts:
            if addr.get_name() == name:
                self.contacts.remove(addr)
                print(f"{name}의 연락처가 삭제되었습니다.")
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")

    def edit_addr(self, name, new_addr):
        for i, addr in enumerate(self.contacts):
            if addr.get_name() == name:
                self.contacts[i] = new_addr
                print(f"{name}의 연락처가 수정되었습니다.")
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")

    def printContact(self):
        contact = Addr()
        contact.showData()

