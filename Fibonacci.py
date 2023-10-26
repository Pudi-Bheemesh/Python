int fibonacci(int n)
{
if(n<=0)
return n; //base case
else //general case
return fibonacci(n-1)+fibonacci(n-2);
}
int main()
{
int num;
printf("Which term of Fibonacci series you want to find: ");
scanf("%d",&num);
printf("%dth term is %d\n",num,
fibonacci(num));
return 0;
}