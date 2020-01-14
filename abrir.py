

def run():
    counter = 0
    with open('aleph.txt', encoding="utf8") as file:
            for line in file:
                counter += line.count('Beatriz')
    print('Beatriz se encuentra {} veces en el texto'.format(counter))
if __name__ == '__main__':
    run()
