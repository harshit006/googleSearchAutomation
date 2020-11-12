import webbrowser
import wikipedia

google = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def search():
    task = input('Tab name = ')
    url = str(task)
    if url == 'youtube':
        webbrowser.get(google).open('youtube.com')
    else:
        webbrowser.get(google).open(
            'https://www.google.com/search?q=' + task + '&rlz=1C1CHBF_enIN891IN891&oq=python&aqs=chrome..69i57j69i59l3j0i433j69i60l3.9666j0j7&sourceid=chrome&ie=UTF-8')


if __name__ == "__main__":
    while True:
        search()
