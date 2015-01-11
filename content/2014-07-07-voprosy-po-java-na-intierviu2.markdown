title: "Вопросы по java на интервью 2"
date: 2014-07-07 14:42:36 +0200
categories: java, вопросы, интервью

Продолжим с вопросами. 

###Как перевернуть строку?
наверно самый популярный вопрос на собеседованиях по java. Естественно от вас не ожидают использования вспомогательных классов типа `StringBuffer`. Есть несколько вариантов решения, я покажу самый простой:
<!--more-->

    :::java
    package com.company;

    public class Main {
        public static String reverseByArray(String s) {
            char[] a = s.toCharArray();
            char[] b = new char[a.length];
            for (int i = 0; i < a.length; i++) {
                b[(a.length - 1) - i] = a[i];
            }
            return new String(b);
        }

        public static void main(String[] args) {
            String string = "Hello world!!";
            System.out.println(reverseByArray(string)); // !!dlrow olleH
        }
    }

###Написать программу которая отсортирует массив методом пузырька

Собственно тут нечего комментировать и так все понятно:

    :::java
    package com.company;

    import java.util.Arrays;

    public class Main {
        public static void main(String args[]) {
            //testing our bubble sort method in Java
            int[] unsorted = {32, 39,21, 45, 23, 3};
            bubbleSort(unsorted);

            //one more testing of our bubble sort code logic in Java
            int[] test = { 5, 3, 2, 1};
            bubbleSort(test);

        }

        public static void bubbleSort(int[] unsorted){
            System.out.println("unsorted array before sorting : " + Arrays.toString(unsorted));

            // Outer loop - need n-1 iteration to sort n elements
            for(int i=0; i<unsorted.length -1; i++){

                //Inner loop to perform comparision and swapping between adjacent numbers
                //After each iteration one index from last is sorted
                for(int j= 1; j<unsorted.length -i; j++){

                    //If current number is greater than swap those two
                    if(unsorted[j-1] > unsorted[j]){
                        int temp = unsorted[j];
                        unsorted[j] = unsorted[j-1];
                        unsorted[j-1] = temp;
                    }
                }
                System.out.printf("unsorted array after %d pass %s: %n", i+1, Arrays.toString(unsorted));
            }
        }
    }

###Написать программу которая выдаст последовательность чисел Фибоначи
Пришлось пару раз написать такую на интервью. В обстановке стресса иногда непросто догадаться об очевидных вещах

    :::java
    package com.company;

    import java.util.Scanner;

    public class Main {
        public static void main(String args[]) {
            //input to print Fibonacci series upto how many numbers
            System.out.println("Enter number upto which Fibonacci series to print: ");
            int number = new Scanner(System.in).nextInt();

            System.out.println("Fibonacci series upto " + number +" numbers : ");
            //printing Fibonacci series upto number
            for(int i=1; i<=number; i++){
                System.out.print(fibonacci2(i) +" ");
            }


        }

        /*
         * Java program for Fibonacci number using recursion.
         * This program uses tail recursion to calculate Fibonacci number for a given number
         * @return Fibonacci number
         */
        public static int fibonacci(int number){
            if(number == 1 || number == 2){
                return 1;
            }

            return fibonacci(number-1) + fibonacci(number -2); //tail recursion
        }

        /*
         * Java program to calculate Fibonacci number using loop or Iteration.
         * @return Fibonacci number
         */
        public static int fibonacci2(int number){
            if(number == 1 || number == 2){
                return 1;
            }
            int fibo1=1, fibo2=1, fibonacci=1;
            for(int i= 3; i<= number; i++){
                fibonacci = fibo1 + fibo2; //Fibonacci number is sum of previous two Fibonacci number
                fibo1 = fibo2;
                fibo2 = fibonacci;

            }
            return fibonacci; //Fibonacci number
        }

    }

###В чем разница между структурами данных Stack и Queue?
Тоже классический вопрос. Я так полагаю все знают на него ответ. Нет? Ок, объясняю :) Stack(стопка) это структура данных типа LIFO(Last In First Out), т.е. стандартная стопка, последнее положил и первая вылетела. В тоже время Queue(очередь) это структура типа FIFO(First In First Out), т.е. стандартная очередь, первый пришел и первый же вышел. Все как в жизни :)


Пока на этом все :) Stay tuned...

