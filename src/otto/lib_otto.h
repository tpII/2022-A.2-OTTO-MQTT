#ifndef Otto_h
#define Otto_h

#include <Servo.h>
#include "Oscillator.h"

//-- Constants
#define FORWARD     1
#define BACKWARD    -1
#define LEFT        1
#define RIGHT       -1
#define SMALL       5
#define MEDIUM      15
#define BIG         30

// -- Servo delta limit default. degree / sec
#define SERVO_LIMIT_DEFAULT 240

class Otto
{
  public:

    //-- Otto initialization
    void init(int pierna_izq, int pierna_der, int pie_der, int pie_izq,int tr, int ec);
    //-- Attach & detach functions
    void attachServos();
    void detachServos();

    //-- Predetermined Motion Functions
    void moveServos(int time, int  servo_target[]);
    void oscillateServos(int A[4], int O[4], int T, double phase_diff[4]);

    //-- HOME = Otto at rest position
    void home();
    bool getRestState(){return isOttoResting;};
    void setRestState(bool state){isOttoResting=state;};


    void walkForward();
    void walkBackward();
    void turnRight();
    void turnLeft();
    void bend ();
    void shakeLeg ();

    void updown();
    void swing(int steps=1, int T=1000,int h=30);
    void swingFix();
    void tiptoeSwing();

    void moonwalker();
    void crusaito();
    void flapping();

    void happy();
    void sad();
    void victory();
    void angry();
    void sleeping();
    void confused();
    void fart();
    void fail();

    void avoidObstacles();
    void followMode();
    void retrieve();
    
    typedef void (Otto::*function) ();
    function doActionsArray [23]={
      &Otto::home,
      &Otto::walkForward,
      &Otto::walkBackward,  
      &Otto::turnRight,
      &Otto::turnLeft,
      &Otto::bend,
      &Otto::shakeLeg,
      &Otto::moonwalker,
      &Otto::crusaito,
      &Otto::flapping,
      &Otto::swingFix,
      &Otto::tiptoeSwing,
      &Otto::updown,
      &Otto::happy,
      &Otto::sad,
      &Otto::victory,
      &Otto::sleeping,
      &Otto::confused,
      &Otto::fart,
      &Otto::fail,
      &Otto::followMode,
      &Otto::retrieve,
      &Otto::avoidObstacles, 
    };

  private:

    Oscillator servo[4];
    int servo_pins[4];
    int trigger;
    int echo;
    unsigned long final_time;
    unsigned long partial_time;
    float increment[4];

    bool isOttoResting;
    long ultrasound();
    void execute(int A[4], int O[4], int T, double phase_diff[4], float steps);

};

#endif
