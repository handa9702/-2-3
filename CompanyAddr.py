from Address import Addr
class CompanyAddr(Addr):
    def __init__(self, name, phone, email ,address, group, birthday, company, department, position):
        super().__init__(name, phone, email ,address, group, birthday, position)
        self.__company = company
        self.__department = department
        

    def get_company(self):
        return self.__company
    def get_department(self):
        return self.__department
    
    
    def print_info(self):
           
           print(f"이름: {self.get_name()}")
           print(f"전화번호: {self.get_phone()}")
           print(f"이메일: {self.get_email()}")
           print(f"주소: {self.get_address()}")
           print(f"생일: {self.get_birthday()}")
           print(f"그룹(회사/거래처): {self.get_group()}")
           print(f"회사이름: {self.get_company()}")
           print(f"부서이름: {self.get_department()}")
           print(f"직급: {self.get_position()}")
