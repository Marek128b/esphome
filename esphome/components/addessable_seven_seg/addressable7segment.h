#pragma once

#include "esphome/core/component.h"
#include "esphome/core/color.h"
#include "esphome/components/display/display_buffer.h"
#include "esphome/components/light/addressable_light.h"

#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

namespace esphome {
namespace addressableSegment {

class addressableSegment : public Component {
 private:
  int PIXEL_PIN;
  int PIXEL_COUNT;
  Adafruit_NeoPixel *pixels;

  void showWithDP(char nr, int SLocation, boolean dp, int brightness);

 public:
  addressableSegment(int pinNr, int segmentCount);
  void begin();

  void showInt(int nr, int location, int brightness);
  void showChar(char ch, int location, int brightness);
  void printString(String str, int SLocation, int brightness);
  void printInt(int nr, int SLocation, int brightness);
  void printInt(unsigned int nr, int SLocation, int brightness);
  void printInt(unsigned long nr, int SLocation, int brightness);
  void SegOff();
  void printDouble(double f, int pres, int SLocation, int brightness);

  void setup() override {
    // Any setup code required by your library
    begin();  // Assuming your library has a `begin` function
  }
};

}  // namespace addressable_segment
}  // namespace esphome
