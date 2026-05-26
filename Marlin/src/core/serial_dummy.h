/**
 * Marlin 3D Printer Firmware
 * Copyright (c) 2020 MarlinFirmware [https://github.com/MarlinFirmware/Marlin]
 *
 * Based on Sprinter and grbl.
 * Copyright (c) 2011 Camiel Gubbels / Erik van der Zalm
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */
#pragma once

#include "serial_base.h"

struct DummySerial {
  DummySerial() {}

  void begin(const long) {}
  void end() {}

  int available() const { return 0; }
  int available(serial_index_t) const { return 0; }

  int read() { return -1; }
  int read(serial_index_t) { return -1; }

  void flush() {}
  size_t write(uint8_t) { return 1; }

  bool connected() const { return true; }
  bool connected() { return true; }

  //SerialFeature features(serial_index_t) const { return SerialFeature::None; }

  operator bool() const { return true; }

  int availableForWrite(void) { return 1; }
};


