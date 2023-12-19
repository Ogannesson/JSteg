# main.py

import stego
import analyze
import extract
import numpy as np


def main_menu():
    while True:
        print("1. 嵌入隐写信息")
        print("2. 提取隐写信息")
        print("3. 分析DCT系数直方图")
        print("4. 退出")
        choice = input("请选择一个操作: ")

        if choice == '1':
            # cover_path = input("请输入封面图像路径: ")
            cover_path = "input/lena.jpg"
            # stego_path = input("请输入隐写图像保存路径: ")
            stego_path = "output/stego.jpg"
            # message_length = int(input("请输入消息长度: "))
            message_length = 100
            message = np.random.randint(0, 2, size=message_length)
            np.savetxt("output/stego_message.txt", message, fmt='%d')
            stego.embed_message(cover_path, stego_path, message)
            print("隐写信息已嵌入.")
        elif choice == '2':
            # stego_path = input("请输入隐写图像路径: ")
            stego_path = "output/stego.jpg"
            # message_length = int(input("请输入消息长度: "))
            message_length = 100
            # save_path = input("请输入提取信息保存路径: ")
            save_path = "output/extract_message.txt"
            message = extract.extract_message(stego_path, message_length)
            np.savetxt(save_path, message, fmt='%d')
            print("隐写信息已提取.")
        elif choice == '3':
            # image_path = input("请输入图像路径: ")
            image_path0 = "input/lena.jpg"
            image_path1 = "output/stego.jpg"
            analyze.plot_dct_histogram(image_path0)
        elif choice == '4':
            break
        else:
            print("无效选择，请重新选择。")


if __name__ == "__main__":
    main_menu()
