#include <wiringPi.h>
#define LED_PIN1 0
#define LED_PIN2 2
#define LED_PIN3 3


int main(void)
{
    wiringPiSetup ();
    //wiringPiSetupGpio();
    pinMode (LED_PIN1, OUTPUT);
    pinMode (LED_PIN2, OUTPUT);
    pinMode (LED_PIN3, OUTPUT);

    digitalWrite(LED_PIN1, HIGH); 
    delay(2000);
    digitalWrite(LED_PIN1, LOW); 
    digitalWrite(LED_PIN2, HIGH); 
    delay(2000);
    digitalWrite(LED_PIN2, LOW); 
    digitalWrite(LED_PIN3, HIGH); 
    delay(2000);
    digitalWrite(LED_PIN3, LOW); 
    delay(2000);


    
    return 0;



}