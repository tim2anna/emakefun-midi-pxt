"""
标准GM音色库和扩展音色库常量定义.
"""


from micropython import const


# Standard GM Sound Bank
# 标准GM音色库
MIDI_TIMBRE_BANK_0: int = const(0)

# Extended Sound Bank
# 扩展音色库
MIDI_TIMBRE_BANK_127: int = const(127)

# Define channel timbre library - note constants for standard GM timbre library.
# ===== 标准GM音色库的音色常量 =====

# Grand Piano
# 大钢琴
MIDI_TIMBRE_BANK_0_GRAND_PIANO: int = const(0)

# Bright Piano
# 明亮钢琴
MIDI_TIMBRE_BANK_0_BRIGHT_PIANO: int = const(1)

# Electric Grand Piano 3
# 电子大钢琴3
MIDI_TIMBRE_BANK_0_ELECTRIC_GRAND_PIANO_3: int = const(2)

# Honky Tonk Piano
# 酒吧钢琴
MIDI_TIMBRE_BANK_0_HONKY_TONK_PIANO: int = const(3)

# Electric Piano 1
# 电钢琴音色1	
MIDI_TIMBRE_BANK_0_ELECTRIC_PIANO_1: int = const(4)

# Electric Piano 2
# 电钢琴音色2
MIDI_TIMBRE_BANK_0_ELECTRIC_PIANO_2: int = const(5)

# Harpsichord
# 大键琴
MIDI_TIMBRE_BANK_0_HARPSICHORD: int = const(6)

# Clavi
# 击弦古钢琴
MIDI_TIMBRE_BANK_0_CLAVI: int = const(7)

# Celesta
# 钢片琴
MIDI_TIMBRE_BANK_0_CELESTA: int = const(8)

# Glockenspiel
# 钟琴
MIDI_TIMBRE_BANK_0_GLOCKENSPIEL: int = const(9)

# Music Box
# 八音盒
MIDI_TIMBRE_BANK_0_MUSIC_BOX: int = const(10)

# Vibraphone
# 颤音琴
MIDI_TIMBRE_BANK_0_VIBRAPHONE: int = const(11)

# Marimba
# 马林巴琴
MIDI_TIMBRE_BANK_0_MARIMBA: int = const(12)

# Xylophone
# 木琴
MIDI_TIMBRE_BANK_0_XYLOPHONE: int = const(13)

# Tubular Bells
# 管钟
MIDI_TIMBRE_BANK_0_TUBULAR_BELLS: int = const(14)

# Dulcimer
# 扬琴
MIDI_TIMBRE_BANK_0_DULCIMER: int = const(15)

# Drawbar Organ
# 拉杆风琴
MIDI_TIMBRE_BANK_0_DRAWBAR_ORGAN: int = const(16)

# Percussive Organ
# 击音管风琴
MIDI_TIMBRE_BANK_0_PERCUSSIVE_ORGAN: int = const(17)

# Rock Organ
# 摇滚风琴
MIDI_TIMBRE_BANK_0_ROCK_ORGAN: int = const(18)

# Church Organ
# 教堂管风琴
MIDI_TIMBRE_BANK_0_CHURCH_ORGAN: int = const(19)

# Reed Organ
# 簧风琴
MIDI_TIMBRE_BANK_0_REED_ORGAN: int = const(20)

# Accordion French
# 法国手风琴
MIDI_TIMBRE_BANK_0_ACCORDION_FRENCH: int = const(21)

# Harmonica
# 口琴
MIDI_TIMBRE_BANK_0_HARMONICA: int = const(22)

# Tango Accordion
# 探戈手风琴
MIDI_TIMBRE_BANK_0_TANGO_ACCORDION: int = const(23)

# Acoustic Guitar Nylon String
# 尼龙弦吉他
MIDI_TIMBRE_BANK_0_ACOUSTIC_GUITAR_NYLON_STRING: int = const(24)

# Acoustic Guitar Steel String
# 钢弦吉他
MIDI_TIMBRE_BANK_0_ACOUSTIC_GUITAR_STEEL_STRING: int = const(25)

# Electric Guitar Jazz
# 爵士电吉他
MIDI_TIMBRE_BANK_0_ELECTRIC_GUITAR_JAZZ: int = const(26)

# Electric Guitar Clean
# 清音电吉他
MIDI_TIMBRE_BANK_0_ELECTRIC_GUITAR_CLEAN: int = const(27)

# Electric Guitar Muted
# 闷音电吉他
MIDI_TIMBRE_BANK_0_ELECTRIC_GUITAR_MUTED: int = const(28)

# Electric Guitar Drive
# 过载电吉他
MIDI_TIMBRE_BANK_0_ELECTRIC_GUITAR_DRIVE: int = const(29)

# Electric Guitar Distortion
# 失真电吉他
MIDI_TIMBRE_BANK_0_ELECTRIC_GUITAR_DISTORTION: int = const(30)

# Guitar Harmonics
# 吉他泛音
MIDI_TIMBRE_BANK_0_GUITAR_HARMONICS: int = const(31)

# Acoustic Bass
# 原声贝斯
MIDI_TIMBRE_BANK_0_ACOUSTIC_BASS: int = const(32)

# Finger Bass
# 指弹贝斯
MIDI_TIMBRE_BANK_0_FINGER_BASS: int = const(33)

# Picked Bass
# 拨片贝斯
MIDI_TIMBRE_BANK_0_PICKED_BASS: int = const(34)

# Fretless Bass
# 无品贝斯
MIDI_TIMBRE_BANK_0_FRETLESS_BASS: int = const(35)

# Slap Bass 1
# 击弦贝斯音色1
MIDI_TIMBRE_BANK_0_SLAP_BASS_1: int = const(36)

# Slap Bass 2
# 击弦贝斯音色2
MIDI_TIMBRE_BANK_0_SLAP_BASS_2: int = const(37)

# Synth Bass 1
# 合成贝斯音色1
MIDI_TIMBRE_BANK_0_SYNTH_BASS_1: int = const(38)

# Synth Bass 2
# 合成贝斯音色2
MIDI_TIMBRE_BANK_0_SYNTH_BASS_2: int = const(39)

# Violin
# 小提琴
MIDI_TIMBRE_BANK_0_VIOLIN: int = const(40)

# Viola
# 小提琴
MIDI_TIMBRE_BANK_0_VIOLA: int = const(41)

# Cello
# 大提琴
MIDI_TIMBRE_BANK_0_CELLO: int = const(42)

# Contrabass
# 低音大提琴
MIDI_TIMBRE_BANK_0_CONTRABASS: int = const(43)

# Tremolo Strings
# 颤音弦乐
MIDI_TIMBRE_BANK_0_TREMOLO_STRINGS: int = const(44)

# Pizzicato Strings
# 拨奏弦乐
MIDI_TIMBRE_BANK_0_PIZZICATO_STRINGS: int = const(45)

# Orchestral Harp
# 管弦乐竖琴
MIDI_TIMBRE_BANK_0_ORCHESTRAL_HARP: int = const(46)

# Timpani
# 定音鼓
MIDI_TIMBRE_BANK_0_TIMPANI: int = const(47)

# String Ensemble 1
# 弦乐合奏音色1	
MIDI_TIMBRE_BANK_0_STRING_ENSEMBLE_1: int = const(48)

# String Ensemble 2
# 弦乐合奏音色2
MIDI_TIMBRE_BANK_0_STRING_ENSEMBLE_2: int = const(49)

# Synth Strings 1
# 合成弦乐音色1
MIDI_TIMBRE_BANK_0_SYNTH_STRINGS_1: int = const(50)

# Synth Strings 2
# 合成弦乐音色2
MIDI_TIMBRE_BANK_0_SYNTH_STRINGS_2: int = const(51)

# Choir Aahs
# 人声合唱"啊"
MIDI_TIMBRE_BANK_0_CHOIR_AAHS: int = const(52)

# Voice Oohs
# 人声合唱"哦"
MIDI_TIMBRE_BANK_0_VOICE_OOHS: int = const(53)

# Synth Voice
# 合成人声
MIDI_TIMBRE_BANK_0_SYNTH_VOICE: int = const(54)

# Orchestra Hit
# 交响打击乐
MIDI_TIMBRE_BANK_0_ORCHESTRA_HIT: int = const(55)

# Trumpet
# 小号
MIDI_TIMBRE_BANK_0_TRUMPET: int = const(56)

# Trombone
# 长号
MIDI_TIMBRE_BANK_0_TROMBONE: int = const(57)

# Tuba
# 大号
MIDI_TIMBRE_BANK_0_TUBA: int = const(58)

# Muted Trumpet
# 弱音小号
MIDI_TIMBRE_BANK_0_MUTED_TRUMPET: int = const(59)

# French Horn
# 法国号
MIDI_TIMBRE_BANK_0_FRENCH_HORN: int = const(60)

# Brass Section
# 铜管组
MIDI_TIMBRE_BANK_0_BRASS_SECTION: int = const(61)

# Synth Brass 1
# 合成铜管音色1
MIDI_TIMBRE_BANK_0_SYNTH_BRASS_1: int = const(62)

# Synth Brass 2
# 合成铜管音色2
MIDI_TIMBRE_BANK_0_SYNTH_BRASS_2: int = const(63)

# Soprano Sax
# 高音萨克斯风
MIDI_TIMBRE_BANK_0_SOPRANO_SAX: int = const(64)

# Alto Sax
# 中音萨克斯风
MIDI_TIMBRE_BANK_0_ALTO_SAX: int = const(65)

# Tenor Sax
# 低音萨克斯风
MIDI_TIMBRE_BANK_0_TENOR_SAX: int = const(66)

# Baritone Sax
# 次低音萨克斯风
MIDI_TIMBRE_BANK_0_BARITONE_SAX: int = const(67)

# Oboe
# 双簧管
MIDI_TIMBRE_BANK_0_OBOE: int = const(68)

# English Horn
# 英国管
MIDI_TIMBRE_BANK_0_ENGLISH_HORN: int = const(69)

# Bassoon
# 巴松管
MIDI_TIMBRE_BANK_0_BASSOON: int = const(70)

# Clarinet
# 单簧管
MIDI_TIMBRE_BANK_0_CLARINET: int = const(71)

# Piccolo
# 短笛
MIDI_TIMBRE_BANK_0_PICCOLO: int = const(72)

# Flute
# 长笛
MIDI_TIMBRE_BANK_0_FLUTE: int = const(73)

# Recorder
# 直笛
MIDI_TIMBRE_BANK_0_RECORDER: int = const(74)

# Pan Flute
# 排笛
MIDI_TIMBRE_BANK_0_PAN_FLUTE: int = const(75)

# Blown Bottle
# 瓶笛
MIDI_TIMBRE_BANK_0_BLOWN_BOTTLE: int = const(76)

# Shakuhachi
# 尺八
MIDI_TIMBRE_BANK_0_SHAKUHACHI: int = const(77)

# Whistle
# 口哨
MIDI_TIMBRE_BANK_0_WHISTLE: int = const(78)

# Ocarina
# 陶笛
MIDI_TIMBRE_BANK_0_OCARINA: int = const(79)

# Square Lead
# 方波主奏
MIDI_TIMBRE_BANK_0_SQUARE_LEAD: int = const(80)

# Sawtooth Lead
# 锯齿波主奏
MIDI_TIMBRE_BANK_0_SAWTOOTH_LEAD: int = const(81)

# Calliope Lead
# 汽笛风琴主奏
MIDI_TIMBRE_BANK_0_CALLIOPE_LEAD: int = const(82)

# Chiff Lead
# 风鸣主奏
MIDI_TIMBRE_BANK_0_CHIFF_LEAD: int = const(83)

# Charang Lead
# 查兰琴主音
MIDI_TIMBRE_BANK_0_CHARANG_LEAD: int = const(84)

# Voice Lead
# 人声主音
MIDI_TIMBRE_BANK_0_VOICE_LEAD: int = const(85)

# Fifths Lead
# 五度音主音
MIDI_TIMBRE_BANK_0_FIFTHS_LEAD: int = const(86)

# Bass Guitar Lead
# 贝斯吉他主音
MIDI_TIMBRE_BANK_0_BASS_GUITAR_LEAD: int = const(87)

# Fantasia Pad
# 幻想音垫
MIDI_TIMBRE_BANK_0_FANTASIA_PAD: int = const(88)

# Warm Pad
# 温暖音垫
MIDI_TIMBRE_BANK_0_WARM_PAD: int = const(89)

# Poly Synth Pad
# 复音合成音垫
MIDI_TIMBRE_BANK_0_POLY_SYNTH_PAD: int = const(90)

# Choir Pad
# 合唱音垫
MIDI_TIMBRE_BANK_0_CHOIR_PAD: int = const(91)

# Bowed Pad
# 弓弦音垫
MIDI_TIMBRE_BANK_0_BOWED_PAD: int = const(92)

# Metallic Pad
# 金属音垫
MIDI_TIMBRE_BANK_0_METALLIC_PAD: int = const(93)

# Halo Pad
# 光环音垫
MIDI_TIMBRE_BANK_0_HALO_PAD: int = const(94)

# Sweep Pad
# 扫掠音垫
MIDI_TIMBRE_BANK_0_SWEEP_PAD: int = const(95)

# Rain FX
# 雨声效果
MIDI_TIMBRE_BANK_0_RAIN_FX: int = const(96)

# Sound Track FX
# 音轨效果
MIDI_TIMBRE_BANK_0_SOUND_TRACK_FX: int = const(97)

# Crystal FX
# 水晶效果
MIDI_TIMBRE_BANK_0_CRYSTAL_FX: int = const(98)

# Atmosphere FX
# 大气效果
MIDI_TIMBRE_BANK_0_ATMOSPHERE_FX: int = const(99)

# Brightness FX
# 明亮效果
MIDI_TIMBRE_BANK_0_BRIGHTNESS_FX: int = const(100)

# Goblins FX
# 哥布林效果
MIDI_TIMBRE_BANK_0_GOBLINS_FX: int = const(101)

# Echoes FX
# 回声效果
MIDI_TIMBRE_BANK_0_ECHOES_FX: int = const(102)

# Sci Fi FX
# 科幻效果
MIDI_TIMBRE_BANK_0_SCI_FI_FX: int = const(103)

# Sitar
# 西塔琴
MIDI_TIMBRE_BANK_0_SITAR: int = const(104)

# Banjo
# 班卓琴
MIDI_TIMBRE_BANK_0_BANJO: int = const(105)

# Shamisen
# 三味线
MIDI_TIMBRE_BANK_0_SHAMISEN: int = const(106)

# Koto
# 古筝
MIDI_TIMBRE_BANK_0_KOTO: int = const(107)

# Kalimba
# 卡林巴琴
MIDI_TIMBRE_BANK_0_KALIMBA: int = const(108)

# Bagpipe
# 风笛
MIDI_TIMBRE_BANK_0_BAGPIPE: int = const(109)

# Fiddle
# 古提琴
MIDI_TIMBRE_BANK_0_FIDDLE: int = const(110)

# Shanai
# 唢呐
MIDI_TIMBRE_BANK_0_SHANAI: int = const(111)

# Tinkle Bell
# 叮当铃
MIDI_TIMBRE_BANK_0_TINKLE_BELL: int = const(112)

# Agogo
# 阿戈戈玲
MIDI_TIMBRE_BANK_0_AGOGO: int = const(113)

# Steel Drums
# 钢鼓
MIDI_TIMBRE_BANK_0_STEEL_DRUMS: int = const(114)

# Woodblock
# 木鱼
MIDI_TIMBRE_BANK_0_WOODBLOCK: int = const(115)

# Taiko Drum
# 太鼓
MIDI_TIMBRE_BANK_0_TAIKO_DRUM: int = const(116)

# Melodic Tom
# 旋律鼓
MIDI_TIMBRE_BANK_0_MELODIC_TOM: int = const(117)

# Synth Drum
# 合成鼓
MIDI_TIMBRE_BANK_0_SYNTH_DRUM: int = const(118)

# Reverse Cymbal
# 反向钹
MIDI_TIMBRE_BANK_0_REVERSE_CYMBAL: int = const(119)

# Guitar Fret Noise
# 吉他品丝噪音
MIDI_TIMBRE_BANK_0_GUITAR_FRET_NOISE: int = const(120)

# Breath Noise
# 呼吸声
MIDI_TIMBRE_BANK_0_BREATH_NOISE: int = const(121)

# Seashore
# 海岸声
MIDI_TIMBRE_BANK_0_SEASHORE: int = const(122)

# Bird Tweet
# 鸟叫声
MIDI_TIMBRE_BANK_0_BIRD_TWEET: int = const(123)

# Telephone Ring
# 电话铃声
MIDI_TIMBRE_BANK_0_TELEPHONE_RING: int = const(124)

# Helicopter
# 直升机声
MIDI_TIMBRE_BANK_0_HELICOPTER: int = const(125)

# Applause
# 掌声
MIDI_TIMBRE_BANK_0_APPLAUSE: int = const(126)

# Gun Shot
# 枪声
MIDI_TIMBRE_BANK_0_GUN_SHOT: int = const(127)

# Define channel timbre library - note constants for expanding timbre library.
# ===== 扩展音色库的音色常量 =====

# Piano 1
# 钢琴音色1
MIDI_TIMBRE_BANK_127_PIANO_1: int = const(0)

# Piano 2
# 钢琴音色2
MIDI_TIMBRE_BANK_127_PIANO_2: int = const(1)

# Piano 3
# 钢琴音色3
MIDI_TIMBRE_BANK_127_PIANO_3: int = const(2)

# Detuned Electric Piano 1
# 失谐电钢琴音色1
MIDI_TIMBRE_BANK_127_DETUNED_ELECTRIC_PIANO_1: int = const(3)

# Electric Piano 1
# 电钢琴音色1
MIDI_TIMBRE_BANK_127_ELECTRIC_PIANO_1: int = const(4)

# Electric Piano 2
# 电钢琴音色2
MIDI_TIMBRE_BANK_127_ELECTRIC_PIANO_2: int = const(5)

# Detuned Electric Piano 2
# 失谐电钢琴音色2
MIDI_TIMBRE_BANK_127_DETUNED_ELECTRIC_PIANO_2: int = const(6)

# Honky Tonk Piano
# 酒吧钢琴
MIDI_TIMBRE_BANK_127_HONKY_TONK: int = const(7)

# Organ 1
# 风琴音色1
MIDI_TIMBRE_BANK_127_ORGAN_1: int = const(8)

# Organ 2
# 风琴音色2
MIDI_TIMBRE_BANK_127_ORGAN_2: int = const(9)

# Organ 3
# 风琴音色3
MIDI_TIMBRE_BANK_127_ORGAN_3: int = const(10)

# Detuned Organ 1
# 失谐风琴音色1
MIDI_TIMBRE_BANK_127_DETUNED_ORGAN_1: int = const(11)

# Church Organ 2
# 教堂风琴音色2
MIDI_TIMBRE_BANK_127_CHURCH_ORGAN_2: int = const(12)

# Church Organ 1
# 教堂风琴音色1
MIDI_TIMBRE_BANK_127_CHURCH_ORGAN_1: int = const(13)

# Church Organ 3
# 教堂风琴音色3
MIDI_TIMBRE_BANK_127_CHURCH_ORGAN_3: int = const(14)

# Accordion French
# 法国手风琴
MIDI_TIMBRE_BANK_127_ACCORDION_FRENCH: int = const(15)

# Harpsichord
# 大键琴
MIDI_TIMBRE_BANK_127_HARPSICHORD: int = const(16)

# Coupled Harpsichord 1
# 耦合羽管键琴音色1
MIDI_TIMBRE_BANK_127_COUPLED_HARPSICHORD_1: int = const(17)

# Coupled Harpsichord 2
# 耦合羽管键琴音色2
MIDI_TIMBRE_BANK_127_COUPLED_HARPSICHORD_2: int = const(18)

# Clavichord 1
# 击弦古钢琴音色1
MIDI_TIMBRE_BANK_127_CLAV_1: int = const(19)

# Clavichord 2
# 击弦古钢琴音色2
MIDI_TIMBRE_BANK_127_CLAV_2: int = const(20)

# Clavichord 3
# 击弦古钢琴音色3
MIDI_TIMBRE_BANK_127_CLAV_3: int = const(21)

# Celesta 1
# 钢片琴音色1
MIDI_TIMBRE_BANK_127_CELESTA_1: int = const(22)

# Celesta 2
# 钢片琴音色2
MIDI_TIMBRE_BANK_127_CELESTA_2: int = const(23)

# Synth Brass 1
# 合成铜管音色1
MIDI_TIMBRE_BANK_127_SYNTH_BRASS_1: int = const(24)

# Synth Brass 2
# 合成铜管音色2
MIDI_TIMBRE_BANK_127_SYNTH_BRASS_2: int = const(25)

# Synth Brass 3
# 合成铜管音色3
MIDI_TIMBRE_BANK_127_SYNTH_BRASS_3: int = const(26)

# Synth Brass 4
# 合成铜管音色4
MIDI_TIMBRE_BANK_127_SYNTH_BRASS_4: int = const(27)

# Synth Bass 1
# 合成贝斯音色1
MIDI_TIMBRE_BANK_127_SYNTH_BASS_1: int = const(28)

# Synth Bass 2
# 合成贝斯音色2
MIDI_TIMBRE_BANK_127_SYNTH_BASS_2: int = const(29)

# Synth Bass 3
# 合成贝斯音色3
MIDI_TIMBRE_BANK_127_SYNTH_BASS_3: int = const(30)

# Synth Bass 4
# 合成贝斯音色4
MIDI_TIMBRE_BANK_127_SYNTH_BASS_4: int = const(31)

# Fantasia
# 幻想音色
MIDI_TIMBRE_BANK_127_FANTASIA: int = const(32)

# Synth Calliope
# 合成汽笛
MIDI_TIMBRE_BANK_127_SYNTH_CALLIOPE: int = const(33)

# Choir Aahs
# 人声合唱"啊"
MIDI_TIMBRE_BANK_127_CHOIR_AAHS: int = const(34)

# Bowed Glass 1
# 弓弦玻璃音色1
MIDI_TIMBRE_BANK_127_BOWED_GLASS_1: int = const(35)

# Soundtrack
# 原声带
MIDI_TIMBRE_BANK_127_SOUNDTRACK: int = const(36)

# Atmosphere
# 氛围音色
MIDI_TIMBRE_BANK_127_ATMOSPHERE: int = const(37)

# Crystal
# 水晶音色
MIDI_TIMBRE_BANK_127_CRYSTAL: int = const(38)

# Bag Pipe
# 风笛
MIDI_TIMBRE_BANK_127_BAG_PIPE: int = const(39)

# Tinkle Bell 1
# 叮当铃音色1
MIDI_TIMBRE_BANK_127_TINKLE_BELL_1: int = const(40)

# Ice Rain 1
# 冰雨音色1
MIDI_TIMBRE_BANK_127_ICE_RAIN_1: int = const(41)

# Oboe 1
# 双簧管音色1
MIDI_TIMBRE_BANK_127_OBOE_1: int = const(42)

# Pan Flute 1
# 排笛音色1
MIDI_TIMBRE_BANK_127_PAN_FLUTE_1: int = const(43)

# Saw Wave
# 锯齿波音色
MIDI_TIMBRE_BANK_127_SAW_WAVE: int = const(44)

# Charang
# 查朗音色
MIDI_TIMBRE_BANK_127_CHARANG: int = const(45)

# Tubular Bells
# 管钟音色
MIDI_TIMBRE_BANK_127_TUBULAR_BELLS: int = const(46)

# Square Wave
# 方波音色
MIDI_TIMBRE_BANK_127_SQUARE_WAVE: int = const(47)

# Strings
# 弦乐音色
MIDI_TIMBRE_BANK_127_STRINGS: int = const(48)

# Tremolo String
# 颤弦音色
MIDI_TIMBRE_BANK_127_TREMOLO_STRING: int = const(49)

# Slow Strings
# 慢弦音色
MIDI_TIMBRE_BANK_127_SLOW_STRINGS: int = const(50)

# Pizzicato String
# 拨奏弦乐
MIDI_TIMBRE_BANK_127_PIZZICATO_STRING: int = const(51)

# Violin
# 小提琴音色
MIDI_TIMBRE_BANK_127_VIOLIN: int = const(52)

# Viola
# 中提琴音色
MIDI_TIMBRE_BANK_127_VIOLA: int = const(53)

# Cello 1
# 大提琴音色1
MIDI_TIMBRE_BANK_127_CELLO_1: int = const(54)

# Cello 2
# 大提琴音色2
MIDI_TIMBRE_BANK_127_CELLO_2: int = const(55)

# Contrabass
# 低音提琴音色
MIDI_TIMBRE_BANK_127_CONTRABASS: int = const(56)

# Harp 1
# 竖琴音色1
MIDI_TIMBRE_BANK_127_HARP_1: int = const(57)

# Harp 2
# 竖琴音色2
MIDI_TIMBRE_BANK_127_HARP_2: int = const(58)

# Nylon String Guitar
# 尼龙弦吉他音色
MIDI_TIMBRE_BANK_127_NYLON_STRING_GUITAR: int = const(59)

# Steel String Guitar
# 钢弦吉他音色
MIDI_TIMBRE_BANK_127_STEEL_STRING_GUITAR: int = const(60)

# Chorus Guitar
# 合唱吉他音色
MIDI_TIMBRE_BANK_127_CHORUS_GUITAR: int = const(61)

# Funk Guitar
# 放克吉他音色
MIDI_TIMBRE_BANK_127_FUNK_GUITAR: int = const(62)

# Sitar
# 西塔琴音色
MIDI_TIMBRE_BANK_127_SITAR: int = const(63)

# Accordion Bass
# 手风琴贝斯
MIDI_TIMBRE_BANK_127_ACCORDION_BASS: int = const(64)

# Fingered Bass
# 指弹贝斯
MIDI_TIMBRE_BANK_127_FINGERED_BASS: int = const(65)

# Picked Bass
# 拨片贝斯
MIDI_TIMBRE_BANK_127_PICKED_BASS: int = const(66)

# Fretless Bass 1
# 无品贝斯音色1
MIDI_TIMBRE_BANK_127_FRETLESS_BASS_1: int = const(67)

# Slap Bass 1
# 击弦贝斯音色1
MIDI_TIMBRE_BANK_127_SLAP_BASS_1: int = const(68)

# Slap Bass 2
# 击弦贝斯音色2
MIDI_TIMBRE_BANK_127_SLAP_BASS_2: int = const(69)

# Fretless Bass 2
# 无品贝斯音色2
MIDI_TIMBRE_BANK_127_FRETLESS_BASS_2: int = const(70)

# Fretless Bass 3
# 无品贝斯音色3
MIDI_TIMBRE_BANK_127_FRETLESS_BASS_3: int = const(71)

# Flute 1
# 长笛音色1
MIDI_TIMBRE_BANK_127_FLUTE_1: int = const(72)

# Flute 2
# 长笛音色2
MIDI_TIMBRE_BANK_127_FLUTE_2: int = const(73)

# Piccolo 1
# 短笛音色1
MIDI_TIMBRE_BANK_127_PICCOLO_1: int = const(74)

# Piccolo 2
# 短笛音色2
MIDI_TIMBRE_BANK_127_PICCOLO_2: int = const(75)

# Recorder
# 竖笛音色
MIDI_TIMBRE_BANK_127_RECORDER: int = const(76)

# Pan Flute 2
# 排笛音色2
MIDI_TIMBRE_BANK_127_PAN_FLUTE_2: int = const(77)

# Soprano Sax
# 高音萨克斯
MIDI_TIMBRE_BANK_127_SOPRANO_SAX: int = const(78)

# Alto Sax
# 中音萨克斯
MIDI_TIMBRE_BANK_127_ALTO_SAX: int = const(79)

# Tenor Sax
# 低音萨克斯
MIDI_TIMBRE_BANK_127_TENOR_SAX: int = const(80)

# Baritone Sax
# 上低音萨克斯
MIDI_TIMBRE_BANK_127_BARITONE_SAX: int = const(81)

# Clarinet 1
# 单簧管音色1
MIDI_TIMBRE_BANK_127_CLARINET_1: int = const(82)

# Clarinet 2
# 单簧管音色2
MIDI_TIMBRE_BANK_127_CLARINET_2: int = const(83)

# Oboe 2
# 双簧管音色2
MIDI_TIMBRE_BANK_127_OBOE_2: int = const(84)

# English Horn
# 英国管
MIDI_TIMBRE_BANK_127_ENGLISH_HORN: int = const(85)

# Bassoon
# 巴松管
MIDI_TIMBRE_BANK_127_BASSOON: int = const(86)

# Harmonica
# 口琴
MIDI_TIMBRE_BANK_127_HARMONICA: int = const(87)

# Trumpet
# 小号
MIDI_TIMBRE_BANK_127_TRUMPET: int = const(88)

# Muted Trumpet
# 弱音小号
MIDI_TIMBRE_BANK_127_MUTED_TRUMPET: int = const(89)

# Trombone 1
# 长号音色1
MIDI_TIMBRE_BANK_127_TROMBONE_1: int = const(90)

# Trombone 2
# 长号音色2
MIDI_TIMBRE_BANK_127_TROMBONE_2: int = const(91)

# French Horn 1
# 法国号音色1
MIDI_TIMBRE_BANK_127_FRENCH_HORN_1: int = const(92)

# French Horn 2
# 法国号音色2
MIDI_TIMBRE_BANK_127_FRENCH_HORN_2: int = const(93)

# Tuba
# 大号
MIDI_TIMBRE_BANK_127_TUBA: int = const(94)

# Brass 1
# 铜管音色1
MIDI_TIMBRE_BANK_127_BRASS_1: int = const(95)

# Brass 2
# 铜管音色2
MIDI_TIMBRE_BANK_127_BRASS_2: int = const(96)

# Vibraphone 1
# 颤音琴音色1
MIDI_TIMBRE_BANK_127_VIBRAPHONE_1: int = const(97)

# Vibraphone 2
# 颤音琴音色2
MIDI_TIMBRE_BANK_127_VIBRAPHONE_2: int = const(98)

# Kalimba
# 卡林巴琴
MIDI_TIMBRE_BANK_127_KALIMBA: int = const(99)

# Tinkle Bell 2
# 叮当铃音色2
MIDI_TIMBRE_BANK_127_TINKLE_BELL_2: int = const(100)

# Glockenspiel
# 钟琴
MIDI_TIMBRE_BANK_127_GLOCKENSPIEL: int = const(101)

# Tubular Bell 2
# 管钟音色2
MIDI_TIMBRE_BANK_127_TUBULAR_BELL_2: int = const(102)

# Xylophone
# 木琴
MIDI_TIMBRE_BANK_127_XYLOPHONE: int = const(103)

# Marimba
# 马林巴琴
MIDI_TIMBRE_BANK_127_MARIMBA: int = const(104)

# Koto
# 古筝
MIDI_TIMBRE_BANK_127_KOTO: int = const(105)

# Taisho Koto
# 太正琴
MIDI_TIMBRE_BANK_127_TAISHO_KOTO: int = const(106)

# Shakuhachi
# 尺八
MIDI_TIMBRE_BANK_127_SHAKUHACHI: int = const(107)

# Whistle 1
# 口哨音色1
MIDI_TIMBRE_BANK_127_WHISTLE_1: int = const(108)

# Whistle 2
# 口哨音色2
MIDI_TIMBRE_BANK_127_WHISTLE_2: int = const(109)

# Blown Bottle
# 瓶笛
MIDI_TIMBRE_BANK_127_BOTTLE_BLOW: int = const(110)

# Pan Flute 3
# 排笛音色3
MIDI_TIMBRE_BANK_127_PAN_FLUTE_3: int = const(111)

# Timpani
# 定音鼓
MIDI_TIMBRE_BANK_127_TIMPANI: int = const(112)

# Melo Tom 1
# 旋律鼓音色1
MIDI_TIMBRE_BANK_127_MELO_TOM_1: int = const(113)

# Melo Tom 2
# 旋律鼓音色2
MIDI_TIMBRE_BANK_127_MELO_TOM_2: int = const(114)

# Synth Drum 1
# 合成鼓音色1
MIDI_TIMBRE_BANK_127_SYNTH_DRUM_1: int = const(115)

# Synth Drum 2
# 合成鼓音色2
MIDI_TIMBRE_BANK_127_SYNTH_DRUM_2: int = const(116)

# Taiko 1
# 太鼓音色1
MIDI_TIMBRE_BANK_127_TAIKO_1: int = const(117)

# Taiko 2
# 太鼓音色2
MIDI_TIMBRE_BANK_127_TAIKO_2: int = const(118)

# Reverse Cymbal
# 反向钹
MIDI_TIMBRE_BANK_127_REVERSE_CYMBAL: int = const(119)

# Castanets
# 响板
MIDI_TIMBRE_BANK_127_CASTANETS: int = const(120)

# Tinkle Bell 3
# 叮当铃音色3
MIDI_TIMBRE_BANK_127_TINKLE_BELL_3: int = const(121)

# Orchestra Hit
# 管弦乐强音
MIDI_TIMBRE_BANK_127_ORCHESTRA_HIT: int = const(122)

# Telephone
# 电话铃声
MIDI_TIMBRE_BANK_127_TELEPHONE: int = const(123)

# Bird
# 鸟叫声
MIDI_TIMBRE_BANK_127_BIRD: int = const(124)

# Helicopter
# 直升机声
MIDI_TIMBRE_BANK_127_HELICOPTER: int = const(125)

# Bowed Glass 2
# 弓弦玻璃音色2
MIDI_TIMBRE_BANK_127_BOWED_GLASS_2: int = const(126)

# Ice Rain 2
# 冰雨音色2
MIDI_TIMBRE_BANK_127_ICE_RAIN_2: int = const(127)
