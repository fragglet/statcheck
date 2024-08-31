
export SOURCE_PORT = $(shell which chocolate-doom)
export SDL_VIDEODRIVER = dummy
export DOOMOPTS = -mb 16 -nodraw -noblit -nosound \
                  -noautoload -nogui -nograbmouse

OUTPUTS = $(subst expected/,output/,$(shell find expected/ -name '*.txt'))
UNZIPOPTS = -L -o

check: expected output
	@diff -x .gitignore -u -r expected output && echo all tests passed

output: $(OUTPUTS)

output/%.txt: demos/%.lmp
	@mkdir -p $(dir $@)
	./testrunner $< $@

extract/%:
	unzip $(UNZIPOPTS) -d extract $< $(notdir $@)

extract/requiem.wad: pwads/requiem.zip
extract/mm2.wad: pwads/mm2.zip
extract/mm.wad: pwads/mm_allup.zip
extract/hr.wad: pwads/hr.zip
extract/av.wad: pwads/av_new.zip
extract/class_ep.wad: pwads/class_ep.zip

clean:
	rm -f extract/*.wad
	rm -rf output/*
