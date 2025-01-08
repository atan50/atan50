//Team MagiMan :: Amanda Tan, Kishi Wijaya
//SoftDev pd4
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

var fact = function(n) {
  if(n == 1){
    return n;
  }
  return (n*fact(n-1));
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fact(1)
fact(2)
fact(3)
//-----------------------------------------------------------------


//fib:

var fib = function(n) {
  if (n == 0){
    return 0;
    if (n == 1){
      return 1;
    }
    return ((fib(n-1)) + (fib(n-2)));
  }
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fib(0)
fib(1)
fib(2)
fib(3)
//=================================================================
