//% weight=100 color=#2494F4 icon="\uf005" block="Emakefun"
//% groups=['MIDI']
//% subcategory="MIDI"
namespace emakefun {

    // MIDI类
    class Midi {

        constructor(tx: SerialPin,  rx: SerialPin) {
            serial.redirect(tx, rx, BaudRate.BaudRate31250);
            basic.pause(50);
        }

        private _write(command: number[]): void {
            serial.writeBuffer(Buffer.fromArray(command));
        }

        private _send_nrpn_or_rpn_parameter(channel: number, most_significant_byte_controller: number, most_significant_byte: number, least_significant_byte_controller: number, least_significant_byte: number, value: number): void {
            this._write([0xB0 | (channel & 0x0F), most_significant_byte_controller, most_significant_byte]);
            this._write([0xB0 | (channel & 0x0F), least_significant_byte_controller, least_significant_byte]);
            this._write([0xB0 | (channel & 0x0F), 0x06, value & 0x7F]);
        }

        private _null_nrpn_or_rpn(channel: number, most_significant_byte_controller: number, least_significant_byte_controller: number): void {
            this._write([0xB0 | (channel & 0x0F), most_significant_byte_controller, 0x7F]);
            this._write([0xB0 | (channel & 0x0F), least_significant_byte_controller, 0x7F]);
        }

        note_on(channel: number, midi_note: number, note_velocity: number): void {
            const command = [0x90 | (channel & 0x0F), midi_note & 0x7F, note_velocity & 0x7F];
            this._write(command);
        }

        note_off(channel: number, midi_note: number): void {
            const command = [0x80 | (channel & 0x0F), midi_note & 0x7F, 0x00];
            this._write(command);
        }

        set_channel_timbre(channel: number, bank: number, timbre: number): void {
            if (bank != 0 && bank != 127) {
                return;
            }
            this._write([0xB0 | (channel & 0x0F), 0x00, bank]);
            this._write([0xC0 | (channel & 0x0F), timbre & 0x7F]);
        }

        set_channel_volume(channel: number, volume: number): void {
            this._write([0xB0 | (channel & 0x0F), 0x07, volume & 0x7F]);
        }

        set_all_channel_volume(volume: number): void {
            this._write([0xF0, 0x7F, 0x7F, 0x04, 0x01, 0x00, volume & 0x7F, 0xF7]);
        }

        set_reverberation(channel: number, reverberation_type: number, reverberation_volume: number, delay_feedback: number): void {
            const command = [0xB0 | (channel & 0x0F), 0x50, reverberation_type & 0x07];
            this._write(command);
            command[1] = 0x5B;
            command[2] = reverberation_volume & 0x7F;
            this._write(command);
            this._write([0xF0, 0x41, 0x10, 0x42, 0x12, 0x40, 0x01, 0x35, delay_feedback & 0x7F, 0x00, 0xF7]);
        }

        set_chorus(channel: number, chorus_effect_type: number, chorus_effect_volume: number, chorus_delay_time: number): void {
            const command = [0xB0 | (channel & 0x0F), 0x51, chorus_effect_type & 0x07];
            this._write(command);
            command[1] = 0x5D;
            command[2] = chorus_effect_volume & 0x7F;
            this._write(command);
            this._write([0xF0, 0x41, 0x10, 0x42, 0x12, 0x40, 0x01, 0x3B, 0x00, 0x00, 0xF7]);
            this._write([0xF0, 0x41, 0x10, 0x42, 0x12, 0x40, 0x01, 0x3C, chorus_delay_time & 0x7F, 0x00, 0xF7]);
        }

        midi_reset(): void {
            this._write([0xFF]);
        }

        channel_all_notes_off(channel: number): void {
            this._write([0xB0 | (channel & 0x0F), 0x7B, 0x00]);
        }

        // 计算音符持续时间（毫秒）
        private _calculate_duration(quarter_num: number, tempo: number): number {
            return (60000 / tempo) * quarter_num;
        }

    }

    // MIDI通道枚举
    export enum MidiChannel {
        //% block="0"
        Channel0 = 0,
        //% block="1"
        Channel1 = 1,
        //% block="2"
        Channel2 = 2,
        //% block="3"
        Channel3 = 3,
        //% block="4"
        Channel4 = 4,
        //% block="5"
        Channel5 = 5,
        //% block="6"
        Channel6 = 6,
        //% block="7"
        Channel7 = 7,
        //% block="8"
        Channel8 = 8,
        //% block="10"
        Channel10 = 10,
        //% block="11"
        Channel11 = 11,
        //% block="12"
        Channel12 = 12,
        //% block="13"
        Channel13 = 13,
        //% block="14"
        Channel14 = 14,
        //% block="15"
        Channel15 = 15,
    }

    // MIDI所有通道枚举
    export enum MidiAllChannel {
        //% block="0"
        Channel0 = 0,
        //% block="1"
        Channel1 = 1,
        //% block="2"
        Channel2 = 2,
        //% block="3"
        Channel3 = 3,
        //% block="4"
        Channel4 = 4,
        //% block="5"
        Channel5 = 5,
        //% block="6"
        Channel6 = 6,
        //% block="7"
        Channel7 = 7,
        //% block="8"
        Channel8 = 8,
        //% block="9打击乐"
        Channel9 = 9,
        //% block="10"
        Channel10 = 10,
        //% block="11"
        Channel11 = 11,
        //% block="12"
        Channel12 = 12,
        //% block="13"
        Channel13 = 13,
        //% block="14"
        Channel14 = 14,
        //% block="15"
        Channel15 = 15,
    }

    export enum MidiNote {
        //% block="C-1"
        C_1 = 0,
        //% block="C#-1"
        CSharp_1 = 1,
        //% block="D-1"
        D_1 = 2,
        //% block="D#-1"
        DSharp_1 = 3,
        //% block="E-1"
        E_1 = 4,
        //% block="F-1"
        F_1 = 5,
        //% block="F#-1"
        FSharp_1 = 6,
        //% block="G-1"
        G_1 = 7,
        //% block="G#-1"
        GSharp_1 = 8,
        //% block="A-1"
        A_1 = 9,
        //% block="A#-1"
        ASharp_1 = 10,
        //% block="B-1"
        B_1 = 11,
        //% block="C0"
        C0 = 12,
        //% block="C#0"
        CSharp0 = 13,
        //% block="D0"
        D0 = 14,
        //% block="D#0"
        DSharp0 = 15,
        //% block="E0"
        E0 = 16,
        //% block="F0"
        F0 = 17,
        //% block="F#0"
        FSharp0 = 18,
        //% block="G0"
        G0 = 19,
        //% block="G#0"
        GSharp0 = 20,
        //% block="A0"
        A0 = 21,
        //% block="A#0"
        ASharp0 = 22,
        //% block="B0"
        B0 = 23,
        //% block="C1"
        C1 = 24,
        //% block="C#1"
        CSharp1 = 25,
        //% block="D1"
        D1 = 26,
        //% block="D#1"
        DSharp1 = 27,
        //% block="E1"
        E1 = 28,
        //% block="F1"
        F1 = 29,
        //% block="F#1"
        FSharp1 = 30,
        //% block="G1"
        G1 = 31,
        //% block="G#1"
        GSharp1 = 32,
        //% block="A1"
        A1 = 33,
        //% block="A#1"
        ASharp1 = 34,
        //% block="B1"
        B1 = 35,
        //% block="C2"
        C2 = 36,
        //% block="C#2"
        CSharp2 = 37,
        //% block="D2"
        D2 = 38,
        //% block="D#2"
        DSharp2 = 39,
        //% block="E2"
        E2 = 40,
        //% block="F2"
        F2 = 41,
        //% block="F#2"
        FSharp2 = 42,
        //% block="G2"
        G2 = 43,
        //% block="G#2"
        GSharp2 = 44,
        //% block="A2"
        A2 = 45,
        //% block="A#2"
        ASharp2 = 46,
        //% block="B2"
        B2 = 47,
        //% block="C3"
        C3 = 48,
        //% block="C#3"
        CSharp3 = 49,
        //% block="D3"
        D3 = 50,
        //% block="D#3"
        DSharp3 = 51,
        //% block="E3"
        E3 = 52,
        //% block="F3"
        F3 = 53,
        //% block="F#3"
        FSharp3 = 54,
        //% block="G3"
        G3 = 55,
        //% block="G#3"
        GSharp3 = 56,
        //% block="A3"
        A3 = 57,
        //% block="A#3"
        ASharp3 = 58,
        //% block="B3"
        B3 = 59,
        //% block="C4"
        C4 = 60,
        //% block="C#4"
        CSharp4 = 61,
        //% block="D4"
        D4 = 62,
        //% block="D#4"
        DSharp4 = 63,
        //% block="E4"
        E4 = 64, 
        //% block="F4"
        F4 = 65,
        //% block="F#4"
        FSharp4 = 66,
        //% block="G4"
        G4 = 67,
        //% block="G#4"
        GSharp4 = 68,
        //% block="A4"
        A4 = 69,
        //% block="A#4"
        ASharp4 = 70,
        //% block="B4"
        B4 = 71,
        //% block="C5"
        C5 = 72,
        //% block="C#5"
        CSharp5 = 73,
        //% block="D5"
        D5 = 74,
        //% block="D#5"
        DSharp5 = 75,
        //% block="E5"
        E5 = 76,
        //% block="F5"
        F5 = 77,
        //% block="F#5"
        FSharp5 = 78,
        //% block="G5"
        G5 = 79,
        //% block="G#5"
        GSharp5 = 80,
        //% block="A5"
        A5 = 81,
        //% block="A#5"
        ASharp5 = 82,
        //% block="B5"
        B5 = 83,
        //% block="C6"
        C6 = 84,
        //% block="C#6"
        CSharp6 = 85,
        //% block="D6"
        D6 = 86,
        //% block="D#6"
        DSharp6 = 87,
        //% block="E6"
        E6 = 88,
        //% block="F6"
        F6 = 89,
        //% block="F#6"
        FSharp6 = 90,
        //% block="G6"
        G6 = 91,
        //% block="G#6"
        GSharp6 = 92,
        //% block="A6"
        A6 = 93,
        //% block="A#6"
        ASharp6 = 94,
        //% block="B6"
        B6 = 95,
        //% block="C7"
        C7 = 96,
        //% block="C#7"
        CSharp7 = 97,
        //% block="D7"
        D7 = 98,
        //% block="D#7"
        DSharp7 = 99,
        //% block="E7"
        E7 = 100,
        //% block="F7"
        F7 = 101,
        //% block="F#7"
        FSharp7 = 102,
        //% block="G7"
        G7 = 103,
        //% block="G#7"
        GSharp7 = 104,
        //% block="A7"
        A7 = 105,
        //% block="A#7"
        ASharp7 = 106,
        //% block="B7"
        B7 = 107,
        //% block="C8"
        C8 = 108,
        //% block="C#8"
        CSharp8 = 109,
        //% block="D8"
        D8 = 110,
        //% block="D#8"
        DSharp8 = 111,
        //% block="E8"
        E8 = 112,
        //% block="F8"
        F8 = 113,
        //% block="F#8"
        FSharp8 = 114,
        //% block="G8"
        G8 = 115,
        //% block="G#8"
        GSharp8 = 116,
        //% block="A8"
        A8 = 117,
        //% block="A#8"
        ASharp8 = 118,
        //% block="B8"
        B8 = 119,
        //% block="C9"
        C9 = 120,
        //% block="C#9"
        CSharp9 = 121,
        //% block="D9"
        D9 = 122,
        //% block="D#9"
        DSharp9 = 123,
        //% block="E9"
        E9 = 124,
        //% block="F9"
        F9 = 125,
        //% block="F#9"
        FSharp9 = 126,
        //% block="G9"
        G9 = 127,
    }

    enum OriNote {
        //% blockIdentity=music.noteFrequency enumval=262
        C = 262,
        //% block=C#
        //% blockIdentity=music.noteFrequency enumval=277
        CSharp = 277,
        //% blockIdentity=music.noteFrequency enumval=294
        D = 294,
        //% blockIdentity=music.noteFrequency enumval=311
        Eb = 311,
        //% blockIdentity=music.noteFrequency enumval=330
        E = 330,
        //% blockIdentity=music.noteFrequency enumval=349
        F = 349,
        //% block=F#
        //% blockIdentity=music.noteFrequency enumval=370
        FSharp = 370,
        //% blockIdentity=music.noteFrequency enumval=392
        G = 392,
        //% block=G#
        //% blockIdentity=music.noteFrequency enumval=415
        GSharp = 415,
        //% blockIdentity=music.noteFrequency enumval=440
        A = 440,
        //% blockIdentity=music.noteFrequency enumval=466
        Bb = 466,
        //% blockIdentity=music.noteFrequency enumval=494
        B = 494,
        //% blockIdentity=music.noteFrequency enumval=131
        C3 = 131,
        //% block=C#3
        //% blockIdentity=music.noteFrequency enumval=139
        CSharp3 = 139,
        //% blockIdentity=music.noteFrequency enumval=147
        D3 = 147,
        //% blockIdentity=music.noteFrequency enumval=156
        Eb3 = 156,
        //% blockIdentity=music.noteFrequency enumval=165
        E3 = 165,
        //% blockIdentity=music.noteFrequency enumval=175
        F3 = 175,
        //% block=F#3
        //% blockIdentity=music.noteFrequency enumval=185
        FSharp3 = 185,
        //% blockIdentity=music.noteFrequency enumval=196
        G3 = 196,
        //% block=G#3
        //% blockIdentity=music.noteFrequency enumval=208
        GSharp3 = 208,
        //% blockIdentity=music.noteFrequency enumval=220
        A3 = 220,
        //% blockIdentity=music.noteFrequency enumval=233
        Bb3 = 233,
        //% blockIdentity=music.noteFrequency enumval=247
        B3 = 247,
        //% blockIdentity=music.noteFrequency enumval=262
        C4 = 262,
        //% block=C#4
        //% blockIdentity=music.noteFrequency enumval=277
        CSharp4 = 277,
        //% blockIdentity=music.noteFrequency enumval=294
        D4 = 294,
        //% blockIdentity=music.noteFrequency enumval=311
        Eb4 = 311,
        //% blockIdentity=music.noteFrequency enumval=330
        E4 = 330,
        //% blockIdentity=music.noteFrequency enumval=349
        F4 = 349,
        //% block=F#4
        //% blockIdentity=music.noteFrequency enumval=370
        FSharp4 = 370,
        //% blockIdentity=music.noteFrequency enumval=392
        G4 = 392,
        //% block=G#4
        //% blockIdentity=music.noteFrequency enumval=415
        GSharp4 = 415,
        //% blockIdentity=music.noteFrequency enumval=440
        A4 = 440,
        //% blockIdentity=music.noteFrequency enumval=466
        Bb4 = 466,
        //% blockIdentity=music.noteFrequency enumval=494
        B4 = 494,
        //% blockIdentity=music.noteFrequency enumval=523
        C5 = 523,
        //% block=C#5
        //% blockIdentity=music.noteFrequency enumval=555
        CSharp5 = 555,
        //% blockIdentity=music.noteFrequency enumval=587
        D5 = 587,
        //% blockIdentity=music.noteFrequency enumval=622
        Eb5 = 622,
        //% blockIdentity=music.noteFrequency enumval=659
        E5 = 659,
        //% blockIdentity=music.noteFrequency enumval=698
        F5 = 698,
        //% block=F#5
        //% blockIdentity=music.noteFrequency enumval=740
        FSharp5 = 740,
        //% blockIdentity=music.noteFrequency enumval=784
        G5 = 784,
        //% block=G#5
        //% blockIdentity=music.noteFrequency enumval=831
        GSharp5 = 831,
        //% blockIdentity=music.noteFrequency enumval=880
        A5 = 880,
        //% blockIdentity=music.noteFrequency enumval=932
        Bb5 = 932,
        //% blockIdentity=music.noteFrequency enumval=988
        B5 = 988,
    }

    // 标准音色库
    export enum StandardTimbre {
        //% block="#0 钢琴"
        MIDI_TIMBRE_BANK_0_GRAND_PIANO = 0,
        //% block="#2 电钢琴"
        MIDI_TIMBRE_BANK_0_ELECTRIC_GRAND_PIANO_3 = 2,
        //% block="#10 八音盒"
        MIDI_TIMBRE_BANK_0_MUSIC_BOX = 10,
        //% block="#11 颤音琴"
        MIDI_TIMBRE_BANK_0_VIBRAPHONE = 11,
        //% block="#12 马林巴琴"
        MIDI_TIMBRE_BANK_0_MARIMBA = 12,
        //% block="#15 扬琴"
        MIDI_TIMBRE_BANK_0_DULCIMER = 15,
        //% block="#19 管风琴"
        MIDI_TIMBRE_BANK_0_CHURCH_ORGAN = 19,
        //% block="#22 口琴"
        MIDI_TIMBRE_BANK_0_HARMONICA = 22,
        //% block="#25 吉他"
        MIDI_TIMBRE_BANK_0_ACOUSTIC_GUITAR_STEEL_STRING = 25,
        //% block="#27 电吉他"  
        MIDI_TIMBRE_BANK_0_ELECTRIC_GUITAR_CLEAN = 27,
        //% block="#32 贝斯"
        MIDI_TIMBRE_BANK_0_ACOUSTIC_BASS = 32,
        //% block="#40 小提琴"
        MIDI_TIMBRE_BANK_0_VIOLIN = 40,
        //% block="#42 大提琴"
        MIDI_TIMBRE_BANK_0_CELLO = 42,
        //% block="#59 长号"
        MIDI_TIMBRE_BANK_0_MUTED_TRUMPET = 59,
        //% block="#65 萨克斯"
        MIDI_TIMBRE_BANK_0_ALTO_SAX = 65,
        //% block="#71 单簧管"
        MIDI_TIMBRE_BANK_0_CLARINET = 71,
        //% block="#73 长笛"
        MIDI_TIMBRE_BANK_0_FLUTE = 73,
        //% block="#79 陶笛"
        MIDI_TIMBRE_BANK_0_OCARINA = 79,
        //% block="#107 古筝"
        MIDI_TIMBRE_BANK_0_KOTO = 107,
        //% block="#111 唢呐"
        MIDI_TIMBRE_BANK_0_SHANAI = 111,
        //% block="#114 钢鼓"
        MIDI_TIMBRE_BANK_0_STEEL_DRUMS = 114,
    }

    // 混响效果类型枚举
    export enum ReverbType {
        //% block="房间1"
        MIDI_REVERBERATION_ROOM_1 = 0,
        //% block="房间2"
        MIDI_REVERBERATION_ROOM_2 = 1,
        //% block="房间3"
        MIDI_REVERBERATION_ROOM_3 = 2,
        //% block="大厅1"
        MIDI_REVERBERATION_HALL_1 = 3,
        //% block="大厅2"
        MIDI_REVERBERATION_HALL_2 = 4,
        //% block="平台"
        MIDI_REVERBERATION_PLATE = 5,
        //% block="延迟"
        MIDI_REVERBERATION_DELAY = 6,
        //% block="声像延迟"
        MIDI_REVERBERATION_PAN_DELAY = 7,
    }

    // 合唱效果类型枚举
    export enum ChorusType {
        //% block="类型1"
        MIDI_CHORUS_1 = 0,
        //% block="类型2"
        MIDI_CHORUS_2 = 1,
        //% block="类型3"
        MIDI_CHORUS_3 = 2,
        //% block="类型4"
        MIDI_CHORUS_4 = 3,
        //% block="反馈式"
        MIDI_CHORUS_FEEDBACK = 4,
        //% block="镶边"
        MIDI_CHORUS_FLANGER = 5,
        //% block="短延迟"
        MIDI_CHORUS_SHORT_DELAY = 6,
        //% block="反馈延迟"
        MIDI_CHORUS_FEEDBACK_DELAY = 7,
    }

    export enum PercussionType {
        //% block="类型1"
        Percussion1 = 0,
        //% block="类型2"
        Percussion2 = 16,
        //% block="类型3"
        Percussion3 = 40,
        //% block="类型4"
        Percussion4 = 48,
        //% block="类型5"
        Percussion5 = 127,
    }

    export enum NoteDuration {
        //% block="1/4节拍"
        Duration_1_4 = 4,
        //% block="1/16节拍"
        Duration_1_16 = 1,
        //% block="1/8节拍"
        Duration_1_8 = 2,
        //% block="1/2节拍"
        Duration_1_2 = 8,
        //% block="3/4节拍"
        Duration_3_4 = 12,
        //% block="1节拍"
        Duration_1 = 16,
        //% block="2节拍"
        Duration_2 = 32,
        //% block="4节拍"
        Duration_4 = 64,
    }

    export enum PercussionNote {
        //% block="D2 军鼓音色1"
        SnareDrum1 = 38,
        //% block="A2 低通鼓"
        LowTom = 45,
        //% block="C#2 边击"
        SideStick = 37,
        //% block="C3 高中通鼓"
        HighMiddleTom = 48,
        //% block="G#2 踏板踩镲"
        PedalHiHat = 44,
        //% block="F2 低地通鼓"
        LowFloorTom = 41,
        //% block="F3 浮音镲碗"
        RideBell = 53,
        //% block="D#2 拍手"
        HandClap = 39,
        //% block="D#5 响棒"
        Claves = 75,
        //% block="F5 低音木鱼"
        LowWoodBlock = 77,
        //% block="G#3 牛铃"
        Cowbell = 56,
        //% block="A5 开放三角铁"
        OpenTriangle = 81,
        //% block="C4 高音邦戈鼓"
        HighBongo = 60,
        //% block="D#4 开放高音康加鼓"
        OpenHighConga = 63,
        //% block="A#4 沙槌"
        Maracas = 70,
        //% block="C#5 短刮瓜"
        ShortGuiro = 73,
        //% block="A#3 颤音叉"
        VibraSlap = 58
    }

    // 全局MIDI实例
    let midiInstance: Midi = null;

    // 全局速度
    let globalTempo: number = 120;

    let globalBankList: number[] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    let globalChannelTimbreList: number[] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

    // 通道
    //% blockId=midi_channel
    //% block="$channel"
    //% timbre.defl='0'
    //% blockHidden=true
    export function midi_channel(channel: MidiChannel): number {
        return channel;
    }

    // 所有通道
    //% blockId=midi_all_channel
    //% block="$channel"
    //% timbre.defl='0'
    //% blockHidden=true
    export function midi_all_channel(channel: MidiAllChannel): number {
        return channel;
    }
    
    // 击打音符
    //% blockId=percussion_note
    //% block="$note"
    //% note.defl='1'
    //% blockHidden=true
    export function percussion_note(note: PercussionNote): number {
        return note;
    }

    // 击打音色类型
    //% blockId=percussion_type
    //% block="$type"
    //% type.defl='1'
    //% blockHidden=true
    export function percussion_type(type: PercussionType): number {
        return type;
    }

    // 标准音色库
    //% blockId=standard_timbre
    //% block="$timbre"
    //% timbre.defl='0'
    //% blockHidden=true
    export function standard_timbre(timbre: StandardTimbre): number {
        return timbre;
    }

    // 节拍，音符持续时间
    //% blockId=note_duration
    //% block="$quarter_num"
    //% quarter_num.defl='4'
    //% blockHidden=true
    export function note_duration(quarter_num: NoteDuration): number {
        return (60000 / globalTempo) * quarter_num / 4;
    }

    // Midi音符
    //% blockId=mapped_note
    //% block="$note"
    //% note.fieldEditor="note"
    //% note.defl='262'
    //% blockHidden=true
    export function mapped_note(note: OriNote): number {
        // 从OriNote频率值映射到MIDI音符值
        const frequencyToMidiMap = {
            131: 48,  // C3
            139: 49,  // CSharp3
            147: 50,  // D3
            156: 51,  // Eb3
            165: 52,  // E3
            175: 53,  // F3
            185: 54,  // FSharp3
            196: 55,  // G3
            208: 56,  // GSharp3
            220: 57,  // A3
            233: 58,  // Bb3
            247: 59,  // B3
            262: 60,  // C (C4)
            277: 61,  // CSharp (C#4)
            294: 62,  // D (D4)
            311: 63,  // Eb (Eb4)
            330: 64,  // E (E4)
            349: 65,  // F (F4)
            370: 66,  // FSharp (F#4)
            392: 67,  // G (G4)
            415: 68,  // GSharp (G#4)
            440: 69,  // A (A4)
            466: 70,  // Bb (Bb4)
            494: 71,  // B (B4)
            523: 72,  // C5
            555: 73,  // CSharp5
            587: 74,  // D5
            622: 75,  // Eb5
            659: 76,  // E5
            698: 77,  // F5
            740: 78,  // FSharp5
            784: 79,  // G5
            831: 80,  // GSharp5
            880: 81,  // A5
            932: 82,  // Bb5
            988: 83   // B5
        };
        
        // 如果找到对应的MIDI值，返回它；否则返回0
        return frequencyToMidiMap[note] || note;
    }

    // 初始化MIDI引脚
    //% blockId="midi_pin_init" block="初始MIDI引脚|$tx"
    //% tx.defl=SerialPin.P0
    //% group="MIDI" weight=99
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_pin_init(tx: SerialPin): void {
        midiInstance = new Midi(tx, tx);

        globalTempo = 120;
        midiInstance.set_all_channel_volume(127);

        globalBankList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        globalChannelTimbreList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        for (let channel = 0; channel < 16; channel++) {
            midiInstance.set_channel_timbre(channel, globalBankList[channel], globalChannelTimbreList[channel])
            midiInstance.set_channel_volume(channel, 127);
        }
        
    }

    // MIDI音符
    //% blockId="midi_note"
    //% block="MIDI音符|$note"
    //% note.fieldEditor="gridpicker"
    //% note.fieldOptions.columns=12
    //% group="MIDI" weight=97
    //% subcategory="MIDI"
    export function midi_note(note: MidiNote): number {
        return note;
    }

    // 击打音符
    //% blockId="midi_play_percussion_note" block="击打|$note|力度|$velocity"
    //% note.shadow="percussion_note"
    //% velocity.min=0 velocity.max=127 velocity.defl=100
    //% group="MIDI" weight=98
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_play_percussion_note(note: number, velocity: number=100): void {
        if (!midiInstance) return;
        // 通道9为打击乐通道
        const channel = 9;
        midiInstance.note_on(channel, note, velocity);
        midiInstance.note_off(channel, note);
    }

    // 通道演奏音符
    //% blockId="midi_play_note" block="通道|$channel|演奏音符|$note|$duration"
    //% channel.shadow="midi_channel"
    //% note.shadow="mapped_note"
    //% duration.shadow="note_duration"
    //% group="MIDI" weight=97
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_play_note(channel: number, note: number, duration: number): void {
        if (!midiInstance) return;
        midiInstance.set_channel_timbre(channel, globalBankList[channel], globalChannelTimbreList[channel]);

        const velocity = 100;
        midiInstance.note_on(channel, note, velocity);
        basic.pause(duration);
        midiInstance.note_off(channel, note);
    }

    // 休止
    //% blockId="midi_rest" block="休止|$duration"
    //% duration.shadow="note_duration"
    //% group="MIDI" weight=96
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_rest(duration: number = 1): void {
        basic.pause(duration);
    }

    // 设置通道乐器
    //% blockId="midi_set_channel_instrument" block="将通道|$channel|的乐器设为|$timbre"
    //% channel.shadow="midi_channel"
    //% timbre.shadow="standard_timbre"
    //% timbre.defl=0
    //% group="MIDI" weight=95
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_channel_instrument(channel: number, timbre: number): void {
        if (!midiInstance) return;
        // 0为基本音色库
        globalChannelTimbreList[channel] = timbre;
        globalBankList[channel] = 0;
        midiInstance.set_channel_timbre(channel, 0, timbre);
    }

    // 设置通道扩展音色
    //% blockId="midi_set_channel_extended_instrument" block="将通道|$channel|的乐器设为扩展音色|#|$timbre"
    //% channel.shadow="midi_channel"
    //% group="MIDI" weight=94
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_channel_extended_instrument(channel: number, timbre: number): void {
        if (!midiInstance) return;
        // 127为扩展音色库
        globalChannelTimbreList[channel] = timbre;
        globalBankList[channel] = 127;
        midiInstance.set_channel_timbre(channel, 127, timbre);
    }

    // 设置打击乐音色类型
    //% blockId="midi_set_percussion_type" block="将打击乐音色类型设为|$timbre"
    //% timbre.shadow="percussion_type"
    //% timbre.defl=0
    //% group="MIDI" weight=93
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_percussion_type(timbre: number): void {
        if (!midiInstance) return;
        // 通道9为打击乐通道，使用扩展音色库
        globalBankList[9] = 127;
        globalChannelTimbreList[9] = timbre;
        midiInstance.set_channel_timbre(9, 127, timbre);
    }

    // 设置通道音量
    //% blockId="midi_set_channel_volume" block="将通道|$channel|音量设为|$volume ％"
    //% channel.shadow="midi_all_channel"
    //% volume.min=0 volume.max=100 volume.defl=100
    //% group="MIDI" weight=92
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_channel_volume(channel: number, volume: number): void {
        if (!midiInstance) return;
        // 将0-100转换为0-127
        const midiVolume = Math.round((volume / 100) * 127);
        midiInstance.set_channel_volume(channel, midiVolume);
    }

    // 设置所有通道音量
    //% blockId="midi_set_all_channel_volume" block="将所有通道音量设为|$volume ％"
    //% volume.min=0 volume.max=100 volume.defl=100
    //% group="MIDI" weight=91
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_all_channel_volume(volume: number): void {
        if (!midiInstance) return;
        // 将0-100转换为0-127
        const midiVolume = Math.round((volume / 100) * 127);
        midiInstance.set_all_channel_volume(midiVolume);
    }

    // 设置演奏速度
    //% blockId="midi_set_tempo" block="将演奏速度设为|$tempo|BPM"
    //% tempo.min=1 tempo.max=300 tempo.defl=120
    //% group="MIDI" weight=90
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_tempo(tempo: number): void {
        globalTempo = tempo;
    }

    // 设置通道混音效果
    //% blockId="midi_set_reverberation" block="将通道|$channel|混音效果|$reverb_type|音量设为|$volume ％|延迟反馈|$feedback ％"
    //% channel.shadow="midi_all_channel"
    //% reverb_type.defl=ReverbType.Room1 reverb_type.options=ReverbType
    //% volume.min=0 volume.max=100 volume.defl=80
    //% feedback.min=0 feedback.max=100 feedback.defl=50
    //% group="MIDI" weight=89
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_reverberation(channel: number, reverb_type: ReverbType, volume: number, feedback: number): void {
        if (!midiInstance) return;
        // 将0-100转换为0-127
        const midiVolume = Math.round((volume / 100) * 127);
        const midiFeedback = Math.round((feedback / 100) * 127);
        midiInstance.set_reverberation(channel, reverb_type, midiVolume, midiFeedback);
    }

    // 设置通道合唱效果
    //% blockId="midi_set_chorus" block="将通道|$channel|合唱效果|$chorus_type|音量设为|$volume ％|延迟|$delay 毫秒"
    //% channel.shadow="midi_all_channel"
    //% chorus_type.defl=ChorusType.Chorus1 chorus_type.options=ChorusType
    //% volume.min=0 volume.max=100 volume.defl=80
    //% delay.min=0 delay.max=2000 delay.defl=5
    //% group="MIDI" weight=88
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_set_chorus(channel: number, chorus_type: ChorusType, volume: number, delay: number): void {
        if (!midiInstance) return;
        // 将0-100转换为0-127
        const midiVolume = Math.round((volume / 100) * 127);
        const midiDelay = Math.round((delay / 100) * 127);
        midiInstance.set_chorus(channel, chorus_type, midiVolume, midiDelay);
    }

    // 重置
    //% blockId="midi_reset" block="MIDI重置"
    //% group="MIDI" weight=87
    //% inlineInputMode=inline
    //% subcategory="MIDI"
    export function midi_reset(): void {
        if (!midiInstance) return;
        midiInstance.midi_reset();
        basic.pause(200)

        globalTempo = 120;
        midiInstance.set_all_channel_volume(127);

        globalBankList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        globalChannelTimbreList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        for (let channel = 0; channel < 16; channel++) {
            midiInstance.set_channel_timbre(channel, globalBankList[channel], globalChannelTimbreList[channel])
            midiInstance.set_channel_volume(channel, 127);
        }
        basic.pause(200);
    }

}
