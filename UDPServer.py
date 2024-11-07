#这是UDP Server端代码，请访问https://github.com/JingQiLiang/Computer-Network-UDP-Socket
from socket import *
# 从 socket 模块中导入所有的公开对象
# 可以直接使用导入的对象，而不需要通过模块名 socket. 来访问它们，可以简化代码
import os
# 导入 os 模块，提供与操作系z统交互的功能函数，执行对文件的管理
# 每次使用都必须用 os. 访问其对象，可以避免代码重名
def recv(udpsocket):
    # 在def自定义函数recv中引入一个UDP套接字udpSocket
    print("-----UDP Server-----")
    # Server端欢迎语
    port = int(input("请输入要绑定的端口号："))
    # 用input接收用户在键盘输入的服务器端口号并存储在变量port里，用int()将输入的字符串转化为整型
    udpsocket.bind(('', port))
    # 使用bind方法将udpSocket绑定到本地地址（空字符串表示本主机所有可用的网络IPv4接口）和用户指定的端口号port
    # 该方法引入的是一个元组( , )
    print("服务器已启动，等待客户端发送数据...")
    save_path = 'recv'
    # 指定当前工作目录下的一个文件夹（目录路径），用于保存接受到的文件，保存该目录路径到字符串变量里
    if not os.path.exists(save_path):
        # 检查save_path指定的目录是否存在
        os.makedirs(save_path)
        # 如果不存在，使用os.makedirs方法创建该目录
    file_name = 'new'  # 指定保存数据的文件名
    # 使用os.path.join方法将目录路径save_path和文件名file_name拼接成一个完整的文件路径，并将其存储在变量path中
    path = os.path.join(save_path, file_name)
    while True:
        # 循环语句用于保持server对client数据的接收
        data, address = udpsocket.recvfrom(40960)
        # 使用udpSocket的recvfrom方法接收数据
        # recvfrom方法返回一个元组，其中包含接收到的数据（字节串）和发送者的地址（元组）
        # 数据的最大接收大小设置为40960个byte
        if data:  # 检查data变量是否包含数据。如果data不为空，表示接收到了数据
            print(f"从{address}接收到数据，正在保存中")
            # 打印接收到数据的来源地址
            # 将接收到的数据写入文件
            with open(path, 'ab') as f:
                # 'ab' 模式表示以二进制追加模式打开path指定的文件。如果文件不存在，它将被创建
                f.write(data)
                # 使用文件对象f的write方法将接收到的数据data写入文件
            print(f"数据已保存到 {path}")
            # 打印数据保存的路径

def main():
    # 创建一个main主函数，作为程序的入口点
    s = socket(AF_INET, SOCK_DGRAM)
    # 创建一个UDP套接字s
    # AF_INET表示用IPv4协议，SOCK_DGRAM表示用UDP协议
    recv(s)
    # 调用函数recv()作为服务端

if __name__ == "__main__":
    main()
    # Python程序的标准入口检查