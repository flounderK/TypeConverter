# TypeConverter
A basic script to perform c type conversions from the command line.

```bash
./typeconverter.py -15.1
u8: lll: 0x33 llh: 0x33 lhl: 0x33 lhh: 0x33 hll: 0x33 hlh: 0x33 hhl: 0x2e hhh: 0xc0
s8: lll: 0x33 llh: 0x33 lhl: 0x33 lhh: 0x33 hll: 0x33 hlh: 0x33 hhl: 0x2e hhh: -0x40
u16: ll: 0x3333 lh: 0x3333 hl: 0x3333 hh: 0xc02e
s16: ll: 0x3333 lh: 0x3333 hl: 0x3333 hh: -0x3fd2
u32: l: 0x33333333 h: 0xc02e3333
s32: l: 0x33333333 h: -0x3fd1cccd
u64: 0xc02e333333333333
s64: -0x3fd1cccccccccccd
f32: l: 4.17232506322307e-08 h: -2.721874952316284
f64: -15.1
```

### Planned future features
 - Actual argparse support
 - Option to specify the type you want to input, specifically so that f32 values can be fully supported
 - Option to specify output type / format. The output is currently very loud.
