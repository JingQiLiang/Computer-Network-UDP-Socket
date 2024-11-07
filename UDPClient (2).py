#这是UDP Client端代码，请访问https://github.com/JingQiLiang/Computer-Network-UDP-Socket
from socket import *
# 从 socket 模块中导入所有的公开对象
# 可以直接使用导入的对象，而不需要通过模块名 socket. 来访问它们，可以简化代码
from os import *
# 导入 os 模块，提供与操作系统交互的功能函数，执行对文件的管理
def send(udpsocket):
    # 在def自定义函数send中引入一个UDP套接字udpSocket
    print("-----UDP Client-----")
    # Client端欢迎语
    ip = input("请输入服务器的IP Address：")
    # 用input接收用户在键盘输入的服务器IP地址并存储在变量ip里
    port = int(input("请输入服务器的Port Number："))
    # 用input接收用户在键盘输入的服务器端口号并存储在变量port里，用int()将输入的字符串转化为整型
    address = (ip, port)
    # 用以上两个变量创建一个server端地址的元组存储在变量address里
    filename = input("请输入要发送的文件名：")
    # 用input接收用户在键盘输入的要发送的文件名并存储在变量name里
    # with语句用于创建一个上下文管理器，它可以确保文件在使用后正确关闭，即使在读取文件过程中发生异常也是如此
    with open(filename, 'rb') as f:  # open函数用于打开一个文件。name是一个变量，包含了要打开的文件的名称或路径
        # 'rb'是模式参数，表示以二进制读取模式打开文件。二进制模式允许读取任何类型的文件，包括文本文件和非文本文件（如图片、音频等）
        # as f 将打开的文件对象临时赋值给变量f，以便在with语句块中使用这个变量来引用文件
        data = f.read()  # 文件对象的方法，用于读取文件的全部内容。读取的内容作为字节串（bytes）返回
        # 将f.read()返回的字节串赋值给变量data，可以在代码中使用data变量来访问文件的内容
    print(f"正在向{address}发送数据")
    # 调用udpsocket对象的sendto方法来发送数据
    sent = udpsocket.sendto(data, address)  # data是要发送的数据，是之前从文件中读取的字节串
    # server_address是服务器的地址和端口号，并作为一个元组
    # sendto方法返回发送的字节数，并将其存储在变量sent中
    print(f"已发送{sent}字节的文件到{address}")  # 告知用户成功发送
    udpsocket.close()  # 完成发送并关闭该套接字

def main():
    # 创建一个main主函数，作为程序的入口点
    s = socket(AF_INET, SOCK_DGRAM)
    # 创建一个UDP套接字s
    # AF_INET表示用IPv4协议，SOCK_DGRAM表示用UDP协议
    send(s)
    # 调用函数send()作为客户端

if __name__ == "__main__":
    main()
    # Python程序的标准入口检查
