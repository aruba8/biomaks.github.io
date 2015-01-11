title: "Вопросы по Java на интервью"
date: 2014-06-22 10:28:14 +0400
categories: java, интервью, вопросы
---
Тестировщиков, а особенно автоматизаторов очень часто на интервью спрашивают про языки программирования. Причем вопросы порой уровнем не ниже middle разработчика. Возникла у меня идея под тэгом `интервью` собирать вопросы которые мне (и не только) задавали на собеседованиях и наверно по возможности буду писать ответы на них. Самые популярные вопросы  это вопросы по алгоритмам и на понимание структур данных.


###Как найти средний элемент в связанном списке за один проход?
<!--more-->
Один из самых популярных вопросов, мне его задавали как минимум трижды, ответил я на него только на третий раз :)
В чем тут трудность? Любой программист и иже с ним, знает как найти средний элемент(есть вариации вопроса, когда просят найти 4й элемент с конца, или 3й и т.д.) за 2 прохода. За первый проход он узнает длинну списка (т.е. перебирает список до тех пор пока не наткнется на `null`), за второй же проход он перебирая список уже наполовину его длинны получает нужный эленмент. А когда просят найти все это дело за один проход, наступает ступор (т.к. собеседования это всетки стресс, и быстро сообразить что-либо трудно). Решение тут простое, необходимо завести 2 указателя. Первый будет увеличиваться (инкрементирорваться :) ппц  какие сложности с англицизмами) каждый элемент, второй каждые 2 элемента. Соответственно когда перый указатель достигнет конца, второй будет указывать на средний элемент.

    :::java
    package com.company;

    public class LinkedListTest {


        public static void main(String args[]) {
            //creating LinkedList with 5 elements including head
            LinkedList linkedList = new LinkedList();
            LinkedList.Node head = linkedList.head();
            linkedList.add( new LinkedList.Node("1"));
            linkedList.add( new LinkedList.Node("2"));
            linkedList.add( new LinkedList.Node("3"));
            linkedList.add( new LinkedList.Node("4"));
            linkedList.add( new LinkedList.Node("5"));
            linkedList.add( new LinkedList.Node("6"));
            linkedList.add( new LinkedList.Node("7"));
            linkedList.add( new LinkedList.Node("8"));
            linkedList.add( new LinkedList.Node("9"));
            linkedList.add( new LinkedList.Node("10"));
            linkedList.add( new LinkedList.Node("11"));
            linkedList.add( new LinkedList.Node("12"));
            linkedList.add( new LinkedList.Node("13"));
            linkedList.add( new LinkedList.Node("14"));
            linkedList.add( new LinkedList.Node("15"));

            //finding middle element of LinkedList in single pass
            LinkedList.Node current = head;
            int length = 0;
            LinkedList.Node middle = head;

            while(current.next() != null){
                length++;
                if(length%2 ==0){
                    middle = middle.next();
                }
                current = current.next();
            }

            if(length%2 == 1){
                middle = middle.next();
            }

            System.out.println("length of LinkedList: " + length);
            System.out.println("middle element of LinkedList : " + middle);

        }

    }

    class LinkedList{
        private Node head;
        private Node tail;

        public LinkedList(){
            this.head = new Node("head");
            tail = head;
        }

        public Node head(){
            return head;
        }

        public void add(Node node){
            tail.next = node;
            tail = node;
        }

        public static class Node{
            private Node next;
            private String data;

            public Node(String data){
                this.data = data;
            }

            public String data() {
                return data;
            }

            public void setData(String data) {
                this.data = data;
            }

            public Node next() {
                return next;
            }

            public void setNext(Node next) {
                this.next = next;
            }

            public String toString(){
                return this.data;
            }
        }
    }

###Что если этот список зациклен?
Этот вопрос возникает как правило после успешного ответа на предыдущий. Собственно ответ вытекает также из предыдущего. Если каждый указатель который мы поддерживаем будет указывать на одну и туже ноду, то это означает что данный список зациклен.

###Как найти 3-й элемент с конца в связанном списке за один проход
Ответ тот же, что и на первый вопрос, только второй указатель должен указывать на 3й элемент от первого

###Есть массив состоящий из элементов типа int от 1 до 100, один из элементов продублирован, как его найти?
Достаточно простой вопрос. Здесь достаточно просто сложить все числа в массиве и вычесть из него сумму массива который не содержит продублированного элемента, в итоге получим искомый элемент.

на этом пока все *to be continued...*

