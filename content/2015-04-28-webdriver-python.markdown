title: "Headless webdriver тесты на python"
date: 2015-04-28 19:36:04 +0400

Небольшая полезняшка тем кто пишет тесты на python и вынужден запускать их headless.

Для запуска тестов нам понадобится `Xvfb`. `Xvfb` [это](http://en.wikipedia.org/wiki/Xvfb) виртуальный Х-сервер который для вывода использует не видеокарту, а оперативную память, так что браузер разницы не заметит.

И еще нам понадобится python библиотека `pyvirtualdisplay`, подробнее о ней [тут](https://pypi.python.org/pypi/PyVirtualDisplay).

устанавливаем `Xvfb`:
    
    :::sh
    sudo apt-get install xvfb

устанавливаем `pyvirtualdisplay`
    
    :::sh
    sudo pip install pyvirtualdisplay

обратите внимание `pyvirtualdisplay` необходимо устанавливать с правами `root`, иначе не заработает

и собственно тест:

    :::python
    from pyvirtualdisplay import Display  
    from selenium import webdriver  
    """visible=0, visible=1 for display or not virual display"""  
    display = Display(visible=0, size= (1024, 768))
    display.start()
    driver= webdriver.Chrome() 
    driver.get('http://qa7.ru')
    print 'The title of current page is: ', driver.title  
    driver.quit()
    display.stop()

Теперь можно, гонять тесты, снимать скриншоты и т.д.
