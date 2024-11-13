from ShowData_Abstract import ShowData

class Addr(ShowData):
    def __init__(self, name, phone, email, address, birthday, group, position):

        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__birthday = birthday
        self.__group = group
        self.__position = position

    def get_name(self):
            return self.__name
    def get_phone(self):
            return self.__phone
    def get_email(self):
            return self.__email
    def get_address(self):
            return self.__address
    def get_birthday(self):
            return self.__birthday
    def get_group(self):
            return self.__group
    def get_position(self):
         return self.__position
        
    def print_info(self):
           print(f"이름: {self.get_name()}")
           print(f"전화번호: {self.get_phone()}")
           print(f"이메일: {self.get_email()}")
           print(f"주소: {self.get_address()}")
           print(f"생일: {self.get_birthday()}")
           print(f"그룹(회사/거래처): {self.get_group()}")
           print(f"직급: {self.get_position()}")

    def showData(self):
           print(f"이름: {self.get_name()}")
           print(f"전화번호: {self.get_phone()}")
           
        
    
            
        