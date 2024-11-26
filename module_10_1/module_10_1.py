import threading
import time


def write_words(word_count, file_name):
    with open('example.txt', 'a', encoding='utf-8') as file:
        file.write(f'Какое-то слово № {word_count}' + '\n')
        time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
func_word = write_words(10, 'example1.txt')
func_word = write_words(30, 'example2.txt')
func_word = write_words(200, 'example3.txt')
func_word = write_words(100, 'example4.txt')
end_time = time.time()
dif_time = end_time - start_time
print(f'Работа потоков {dif_time}')

start_time_thread = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread1.start()
thread1.join()

thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread2.start()
thread2.join()

thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread3.start()
thread3.join()

thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread4.start()
thread4.join()
end_time_thread = time.time()
dif_time_thread = end_time_thread - start_time_thread
print(f'Работа потоков {dif_time_thread}')
