class  Encryptor():
    def encrypt(self,text):
        raise NotImplementedError # fun is not implementrd yet
    def decrypt(self,text):
        raise NotImplementedError

class CaesarEncryptor(Encryptor):
    def __init__(self,shift=3):
        self.shift = shift

    def encrypt(self,text):
        result = ''
        for char in text :
            result += chr((ord(char)+self.shift)%256)
        return result

    def decrypt(self,text):
            result = ''
            for char in text:
                result += chr((ord(char) - self.shift) % 256)
            return result

class User:
    def __init__(self,name):
        self.name = name

class Message:
    def __init__(self,sender,receiver,encrypted_text):
        self.sender = sender
        self.receiver = receiver
        self.encrypted_text = encrypted_text

class ChatRoom:
    def __init__(self,encryptor):
        self.encryptor = encryptor
        self.message = []
    def send(self,sender,reciver,text):
        encrypted = self.encryptor.encrypt(text)
        msg = Message(sender,reciver,encrypted)
        self.message.append(msg)
        print(f"Message sent from {sender.name} --> {reciver.name}")
        print("<---------------------------------------------------->")
    def show_conversation(self,User1 ,User2):
        print(f"chat btween {User1.name} and {User2.name}")
        for msg in self.message:
            if (msg.sender == User1 and msg.receiver== User2) or (msg.sender == User2 and msg.receiver == User1):
                decrypted = self.encryptor.decrypt(msg.encrypted_text)
                print(f"{msg.sender.name} --> {msg.receiver.name}:{decrypted}")
                print(f"Encrypted: {msg.encrypted_text}")# print encrypted text
                print(f"Decrypted: {decrypted}\n")# print decrypted text
                print("...................................................")
user1 = User("parul")
user2 = User("ram")

encryptor = CaesarEncryptor()
chat = ChatRoom(encryptor)
chat.send(user1,user2,"hii ram how are you?")
chat.send(user1,user2,"i'm good what abhout you")
chat.send(user1,user2,"learning python these days")

chat.show_conversation(user1,user2)




