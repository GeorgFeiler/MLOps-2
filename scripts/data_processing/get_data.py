import os
import kaggle

def download_kaggle_dataset():
    # Установите рабочую директорию для скачивания
    download_dir = 'data/raw'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Укажите название соревнования
    competition = 'titanic'

    # Скачайте файлы train.csv и test.csv
    kaggle.api.competition_download_file(competition, 'train.csv', path=download_dir)
    kaggle.api.competition_download_file(competition, 'test.csv', path=download_dir)

    # Разархивируйте скачанные файлы
    os.system(f'unzip -o {download_dir}/train.csv.zip -d {download_dir}')
    os.system(f'unzip -o {download_dir}/test.csv.zip -d {download_dir}')

    # Удалите zip-файлы после разархивирования
    os.remove(f'{download_dir}/train.csv.zip')
    os.remove(f'{download_dir}/test.csv.zip')

if __name__ == '__main__':
    download_kaggle_dataset()

