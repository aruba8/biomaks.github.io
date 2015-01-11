title: "Как запустить браузер с нужным плагином [WebDriver]"
date: 2014-03-09 15:09:03 +0400
categories: selenium, webdriver, hacks

Продолжаю капитанить :) на самом деле пишу больше для себя чтобы потом быстро найти.
Как известно webdriver всегда запускает новый чистый профиль Firefox и прогоняет на нем тесты. Однако иногда не лишнее иметь в этом браузере плагин типа firebug, чтобы быстренько что-либо посмотреть "глазами webdriver" на тестируемой странице. 
Делается это просто, необходимо иметь на машине где запускается браузер, плагин с расширением `.xpi` например `firebug-1.12.7-fx.xpi`.

```java WebdriverConfig.java
FirefoxProfile profile = new FirefoxProfile();
profile.addExtension(new File(pathToExtension));
profile.setPreference("extensions.firebug.currentVersion", "X.X.X");
WebDriver driver = new FirefoxDriver(profile);
```
<!--more-->

где `pathToExtension` - путь к расширению с расширением `.xpi`
в строке `profile.setPreference("extensions.firebug.currentVersion", "X.X.X");` вместо `X.X.X` нужно написать версию плагина больше чем тот который мы устанавливаем, например: `profile.setPreference("extensions.firebug.currentVersion", "1.12.8");`. Это нужно для того чтобы браузер не открывал страницу с описанием плагина.

