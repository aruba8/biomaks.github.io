title: "Опять начал ковырять JavaScript"
date: 2014-01-18 12:24:07 +0400
categories: javascript, money, github, balloon

Есть у меня проектик на [Github](https://github.com/biomaks/money) я его перенес с Bitbucket на всеобщее обозрение. Затеял я его в целях изучения технологий java, javascript, mongo и т.д. Ну так вот, периодически, примерно раз в 2 месяца, я сажусь за него и пытаюсь реализовать чтонибудь. По сути этот проект представляет собой web приложение которое помогает вести учет личных финансов. При написании его я использовал следующие технологии:
<!--more-->

* Java
* Maven
* [Spark](http://www.sparkjava.com/)
* [Freemarker](http://freemarker.org/)
* MongoDB
* JQuery
* JavaScript

Вот  в этот раз мне ударило в голову переписать Категории, это тот функционал который позволяет добавлять различные категории трат и доходов пользователю. Решил использовать js библиотечку, а точнее jquery плагин [jquery.balloon.js](http://file.urin.take-uma.net/jquery.balloon.js-Demo.html), она позволяет создавать по наведению на элемент так называемый balloon, облочко в котором что-то написано.

В принцепе на демо-странице все понятно описано, но я все же приведу пример:
Во первых элемент должен иметь title, по умолчанию отображается в облачке именно он, либо нужно передать в метод ballon опцию: 
    
    content: 'some content'  

Пример создания простого облачка:

    $('.sample2').balloon({ position: "bottom right" });

Плагин очень легкий, и позволяет достаточно гибкие настройки. Например содержимое облачка: 

	contents: null,
	url: null,
	ajaxComplete: null,
	classname: null,
	position: "top",
	offsetX: 0,
	offsetY: 0,
	tipSize: 12,
	delay: 0,
	minLifetime: 200,
	showDuration: 100,
	showAnimation: null,
	hideDuration: 80,
	hideAnimation: function (d) { this.fadeOut(d); }

Или CSS которое передается в метод baloon как опция: 

	css: {
	  minWidth: "20px",
	  padding: "5px",
	  borderRadius: "6px",
	  border: "solid 1px #777",
	  boxShadow: "4px 4px 4px #555",
	  color: "#666",
	  backgroundColor: "#efefef",
	  opacity: "0.85",
	  zIndex: "32767",
	  textAlign: "left"
	}




