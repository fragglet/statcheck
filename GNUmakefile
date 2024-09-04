#
# Copyright (C) 2024 Simon Howard
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version. This program is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

export SOURCE_PORT = $(shell which chocolate-doom)
export SDL_VIDEODRIVER = dummy
export DOOMOPTS = -mb 16 -nodraw -noblit -nosound \
                  -noautoload -nogui -nograbmouse

ALL_DEMOS = $(patsubst %,demos/%,$(shell cat demos.txt))
OUTPUTS = $(subst .lmp,.txt,$(subst demos/,output/,$(ALL_DEMOS)))
UNZIPOPTS = -L -o

check: expected output
	diff -x .gitignore -u -r expected output
	@echo all tests passed

output: $(OUTPUTS)

output/%.txt: demos/%.lmp $(SOURCE_PORT)
	@mkdir -p $(dir $@)
	@./testrunner $< $@

.rules: makerules
	./makerules $@

extract/%:
	unzip $(UNZIPOPTS) -d extract $< $(notdir $@)
	@touch $@

extract/requiem.wad: pwads/requiem.zip
extract/mm2.wad: pwads/mm2.zip
extract/mm.wad: pwads/mm_allup.zip
extract/hr.wad: pwads/hr.zip
extract/av.wad: pwads/av_new.zip
extract/class_ep.wad: pwads/class_ep.zip

clean:
	rm -f extract/*.wad
	rm -rf output/*
	rm -f .rules

include .rules
