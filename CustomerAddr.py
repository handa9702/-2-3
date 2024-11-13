from Address import Addr
class CustomerAddr(Addr):
    def __init__(self, name, phone, email ,address, group, birthday, customer, item, position):
        super().__init__(name, phone, email ,address, group, birthday, position)
        self.__customer = customer
        self.__item = item
        
    def get_customer(self):
        return self.__customer
    def get_item(self):
        return self.__item
    
    def print_info(self):
           
           print(f"이름: {self.get_name()}")
           print(f"전화번호: {self.get_phone()}")
           print(f"이메일: {self.get_email()}")
           print(f"주소: {self.get_address()}")
           print(f"생일: {self.get_birthday()}")
           print(f"그룹(회사/거래처): {self.get_group()}")
           print(f"거래처이름: {self.get_customer()}")
           print(f"품목이름: {self.get_item()}")
           print(f"직급: {self.get_position()}")