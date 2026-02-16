import time
from microbit import *

class Midi:
    def __init__(self, tx):
        """
        MIDI接口初始化

        Args:
            tx: 数据传输引脚.
        """
        uart.init(31250, tx=tx)
        time.sleep_ms(50)

    def _write(self, command):
        """
        向设备发送MIDI命令.

        Args:
            command: 要发送的MIDI命令字节.
        """
        uart.write(bytearray(command))

    def _send_nrpn_or_rpn_parameter(self, channel, most_significant_byte_controller, most_significant_byte, least_significant_byte_controller, least_significant_byte, value):
        """
        向指定通道发送NRPN（未注册参数编号）或RPN（已注册参数编号）参数值.

        Args:
            channel: 指定的通道（0-15）.
            most_significant_byte_controller: 高字节控制器编号（0x63/NRPN或0x65/RPN）.
            most_significant_byte: 参数类别高字节.
            least_significant_byte_controller: 低字节控制器编号（0x62/NRPN或0x64/RPN）.
            least_significant_byte: 特定参数的低字节.
            value: 要设置的参数值（0-127）.
        """
        self._write([0xB0 | (channel & 0x0F), most_significant_byte_controller, most_significant_byte])
        self._write([0xB0 | (channel & 0x0F), least_significant_byte_controller, least_significant_byte])
        self._write([0xB0 | (channel & 0x0F), 0x06, value & 0x7F])

    def _null_nrpn_or_rpn(self, channel, most_significant_byte_controller, least_significant_byte_controller):
        """
        取消当前选择的NRPN/RPN参数（空参数选择），以防止未来的数据输入命令错误修改当前参数.

        Args:
            channel: 指定的通道（0-15）.
            most_significant_byte_controller: 高字节控制器编号（0x63/NRPN或0x65/RPN）.
            least_significant_byte_controller: 低字节控制器编号（0x62/NRPN或0x64/RPN）.
        """
        self._write([0xB0 | (channel & 0x0F), most_significant_byte_controller, 0x7F])
        self._write([0xB0 | (channel & 0x0F), least_significant_byte_controller, 0x7F])

    def note_on(self, channel, midi_note, note_velocity):
        """
        在指定通道上生成给定的MIDI音符.

        Args:
            channel: 指定的通道（0-15）.
            midi_note: MIDI音符（0-127），请参考midi_note.py；其中，通道9的音符请参考midi_percussion_note.py .
            note_velocity: 音符速度（0-127），控制音符的音量和音色亮度，在键盘上对应于按键的硬度，0：静音（相当于noteOff），1-126：从弱到强，127：最大强度.
        """
        self._write([0x90 | (channel & 0x0F), midi_note & 0x7F, note_velocity & 0x7F])

    def note_off(self, channel, midi_note):
        """
        在指定通道上关闭先前使用noteOn()命令在给定音高上打开的音符.

        Args:
            channel: 指定的通道（0-15）.
            midi_note: MIDI音符（0-127），请参考midi_note.py；其中，通道9的音符请参考midi_percussion_note.py.
        """
        self._write([0x80 | (channel & 0x0F), midi_note & 0x7F, 0x00])

    def set_channel_timbre(self, channel, bank, timbre):
        """
        在指定通道上设置音色. 其中，通道9是一个专用鼓组通道，通道9的音色和音符请参考midi_percussion_note.py .

        Args:
            channel: 指定的通道（0-15），其中通道9是一个专用鼓组通道.
            bank: 音色库选择，参数值为MIDI_TIMBRE_BANK_0或MIDI_TIMBRE_BANK_127.
            timbre: 音色编号（0-127），请参考参考midi_timbre.py中的宏（例如MIDI_TIMBRE_BANK_0_GRAND_PIANO）；其中，通道9的音色请参考midi_percussion_note.py .
        """
        if bank != 0 and bank != 127:
            print("Error: bank parameter error, can only be MIDI_TIMBRE_BANK_0 or MIDI_TIMBRE_BANK_127.")
            return
        self._write([0xB0 | (channel & 0x0F), 0x00, bank])
        self._write([0xC0 | (channel & 0x0F), timbre & 0x7F])

    def pitch_bend(self, channel, pitch_bend_value):
        """
        在指定通道上调整音高，默认音高变化范围为±1半音.

        Args:
            channel: 指定的通道（0-15）.
            pitch_bend_value: 音高调整值（0-1023），0：最大向下调整，512：中心位置（无调整），1023：最大向上调整.
        """
        mapped_value = int(min(pitch_bend_value, 1023) * 0x3FFF / 1023)
        self._write([0xE0 | (channel & 0x0F), mapped_value & 0x7F, mapped_value >> 7])

    def pitch_bend_range(self, channel, pitch_bend_range_value):
        """
        在指定通道上设置音高调整范围（灵敏度）.

        Args:
            channel: 指定的通道（0-15）.
            pitch_bend_range_value: 音高调整范围值（半音数，0-127），典型值：1-24（半音），默认值：2（± 2半音）.
        """
        self._send_nrpn_or_rpn_parameter(channel, 0x65, 0x00, 0x64, 0x00, pitch_bend_range_value)
        self._null_nrpn_or_rpn(channel, 0x65, 0x64)

    def midi_reset(self):
        """
        在所有连接的MIDI设备上发送MIDI系统重置命令（0xFF），将所有设备重置为其初始状态.
        """
        self._write([0xFF])

    def channel_all_notes_off(self, channel):
        """
        在指定通道上发送每个音符的noteOff()命令，关闭该通道上所有正在播放的音符.

        Args:
            channel: 指定的通道（0-15）.
        """
        self._write([0xB0 | (channel & 0x0F), 0x7B, 0x00])

    def set_channel_volume(self, channel, volume):
        """
        在指定通道上设置音量.

        Args:
            channel: 指定的通道（0-15）.
            volume: 音量等级（0-127），0：静音，127：最大音量.
        """
        self._write([0xB0 | (channel & 0x0F), 0x07, volume & 0x7F])

    def set_all_channel_volume(self, volume):
        """
        在所有通道上设置音量.

        Args:
            volume: 音量等级（0-127），0：静音，127：最大音量.
        """
        self._write([0xF0, 0x7F, 0x7F, 0x04, 0x01, 0x00, volume & 0x7F, 0xF7])

    def set_reverberation(self, channel, reverberation_type, reverberation_volume, delay_feedback):
        """
        在指定通道上应用混响效果.

        Args:
            channel: 指定的通道（0-15）.
            reverberation_type: 混响效果类型，参考midi_chorus_reverberation.py中的定义（例如MIDI_REVERBERATION_ROOM_1）.
            reverberation_volume: 混响效果音的响度（0-127），0：无混响，127：最大响度.
            delay_feedback: 延迟反馈量（0-127），0：无反馈，127：最大反馈.
        """
        command = [0xB0 | (channel & 0x0F), 0x50, reverberation_type & 0x07]
        self._write(command)
        command[1], command[2] = 0x5B, reverberation_volume & 0x7F
        self._write(command)
        self._write([0xF0, 0x41, 0x10, 0x42, 0x12, 0x40, 0x01, 0x35, delay_feedback & 0x7F, 0x00, 0xF7])

    def set_chorus(self, channel, chorus_effect_type, chorus_effect_volume, chorus_effect_feedback, chorus_delay_time):
        """
        在指定通道上应用合唱效果.

        Args:
            channel: 指定的通道（0-15）.
            chorus_effect_type: 合唱效果类型，参考midi_chorus_reverberation.py中的宏（例如MIDI_CHORUS_1）.
            chorus_effect_volume: 合唱效果的响度（0-127），0：无合唱效果，127：最大响度.
            chorus_effect_feedback: 合唱效果反馈量（0-127，0表示未设置）.
            chorus_delay_time: 合唱延迟时间（0-127，0表示未设置），单位：毫秒.
        """
        command = [0xB0 | (channel & 0x0F), 0x51, chorus_effect_type & 0x07]
        self._write(command)
        command[1], command[2] = 0x5D, chorus_effect_volume & 0x7F
        self._write(command)
        self._write([0xF0, 0x41, 0x10, 0x42, 0x12, 0x40, 0x01, 0x3B, chorus_effect_feedback & 0x7F, 0x00, 0xF7])
        self._write([0xF0, 0x41, 0x10, 0x42, 0x12, 0x40, 0x01, 0x3C, chorus_delay_time & 0x7F, 0x00, 0xF7])

    def set_pan_position(self, channel, pan_position_value):
        """
        在指定通道上设置平衡位置.

        Args:
            channel: 指定的通道（0-15）.
            pan_position_value: 平衡位置值（0-127），0：最左（完全左声道），64：中心位置（平衡左声道和右声道），127：最右（完全右声道）.
        """
        self._write([0xB0 | (channel & 0x0F), 0x0A, pan_position_value & 0x7F])

    def set_equalizer(self, channel, low_frequency_gain, medium_low_frequency_gain, medium_high_frequency_gain, high_frequency_gain, low_frequency, medium_low_frequency, medium_high_frequency, high_frequency):
        """
        在指定通道上设置四段均衡器.

        Args:
            channel: 指定的通道（0-15）.
            low_frequency_gain: 低音增益值（0-127）.
            medium_low_frequency_gain: 中低音增益值（0-127）.
            medium_high_frequency_gain: 中高音增益值（0-127）.
            high_frequency_gain: 高音增益值（0-127）.
            low_frequency: 低音中心值（0-127）.
            medium_low_frequency: 中低音中心值（0-127）.
            medium_high_frequency: 中高音中心值（0-127）.
            high_frequency: 高音中心值（0-127）.
        """
        for param, value in [(0x00, low_frequency_gain), (0x01, medium_low_frequency_gain), (0x02, medium_high_frequency_gain), (0x03, high_frequency_gain), (0x08, low_frequency), (0x09, medium_low_frequency), (0x0A, medium_high_frequency), (0x0B, high_frequency)]:
            self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x37, 0x62, param, value)
        self._null_nrpn_or_rpn(channel, 0x63, 0x62)

    def set_tuning(self, channel, fine_tuning, coarse_tuning):
        """
        在指定通道上设置音调（粗调/微调）.

        Args:
            channel: 指定的通道（0-15）.
            fine_tuning: 微调值（0-127），影响音高的细微变化.
            coarse_tuning: 粗调值（0-127），影响音高的八度变化.
        """
        self._send_nrpn_or_rpn_parameter(channel, 0x65, 0x00, 0x64, 0x01, fine_tuning)
        self._send_nrpn_or_rpn_parameter(channel, 0x65, 0x00, 0x64, 0x02, coarse_tuning)
        self._null_nrpn_or_rpn(channel, 0x65, 0x64)

    def set_vibrato(self, channel, vibrato_rate, vibrato_depth, vibrato_delay_modify):
        """
        在指定通道上设置颤音参数.

        Args:
            channel: 指定的通道（0-15）.
            vibrato_rate: 颤音速率（0-127），控制颤音振荡的速度.
            vibrato_depth: 颤音深度（0-127），控制颤音振荡的振幅.
            vibrato_delay_modify: 颤音延迟修改（0-127），控制颤音开始前的延迟时间.
        """
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x08, vibrato_rate)
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x09, vibrato_depth)
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x0A, vibrato_delay_modify)
        self._null_nrpn_or_rpn(channel, 0x63, 0x62)

    def set_time_varying_filter(self, channel, cutoff, resonance):
        """
        在指定通道上设置时变滤波器（TVF）.

        Args:
            channel: 指定的通道（0-15）.
            cutoff: 截止频率值（0-127），控制滤波器通过的频率范围.
            resonance: 谐振峰/谐振值（0-127），控制滤波器在截止频率附近的增益.
        """
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x20, cutoff)
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x21, resonance)
        self._null_nrpn_or_rpn(channel, 0x63, 0x62)

    def set_envelope(self, channel, attack_time, attenuation_time, release_time):
        """
        在指定通道上设置环境参数.

        Args:
            channel: 指定的通道（0-15）.
            attack_time: 开始时间（0-127），控制声音从零到达最大振幅的时间，单位：毫秒.
            attenuation_time: 衰减时间（0-127），控制声音从最大振幅衰减到保持电平的时间，单位：毫秒.
            release_time: 释放时间（0-127），控制声音释放后音量衰减到零的时间，单位：毫秒.
        """
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x63, attack_time)
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x64, attenuation_time)
        self._send_nrpn_or_rpn_parameter(channel, 0x63, 0x01, 0x62, 0x66, release_time)
        self._null_nrpn_or_rpn(channel, 0x63, 0x62)

    def set_scale_tuning(self, channel, note_c, note_c_sharp, note_d, note_d_sharp, note_e, note_f, note_f_sharp, note_g, note_g_sharp, note_a, note_a_sharp, note_b):
        """
        在指定通道上设置12个音阶调参（每个半音独立调参）.

        Args:
            channel: 指定的通道（0-15）.
            scale_tuning_parameter: 设置12个音阶调参（每个半音独立调参）.
            note_c: C 音符微调值（0-127）.
            note_c_sharp: C# 音符微调值（0-127）.
            note_d: D 音符微调值（0-127）.
            note_d_sharp: D# 音符微调值（0-127）.
            note_e: E 音符微调值（0-127）.
            note_f: F 音符微调值（0-127）.
            note_f_sharp: F# 音符微调值（0-127）.
            note_g: G 音符微调值（0-127）.
            note_g_sharp: G# 音符微调值（0-127）.
            note_a: A 音符微调值（0-127）.
            note_a_sharp: A# 音符微调值（0-127）.
            note_b: B 音符微调值（0-127）.
        """
        self._write([0xF0, 0x41, 0x00, 0x42, 0x12, 0x40, 0x10 | (channel & 0x0F), 0x40, note_c & 0x7F, note_c_sharp & 0x7F, note_d & 0x7F, note_d_sharp & 0x7F, note_e & 0x7F, note_f & 0x7F, note_f_sharp & 0x7F, note_g & 0x7F, note_g_sharp & 0x7F, note_a & 0x7F, note_a_sharp & 0x7F, note_b & 0x7F, 0xF7])

    def set_modulation_wheel(self, channel, high_pitch_volume, time_varying_timbre_cutoff, amplitude, low_frequency_oscillator_rate, pitch_depth, time_varying_filter_depth, time_varying_amplifier_depth):
        """
        在指定通道上设置调制轮参数并配置调制轮声音的多个控制效果.

        Args:
            channel: 指定的通道（0-15）.
            high_pitch_volume: 高音音量强度（0-127）.
            time_varying_timbre_cutoff: 时变音色截止频率（0-127）.
            amplitude: 振幅调制深度（0-127）.
            low_frequency_oscillator_rate: 低频率振荡器速率（0-127）.
            pitch_depth: 音高调制深度（0-127）.
            time_varying_filter_depth: 时变滤波器深度（0-127）.
            time_varying_amplifier_depth: 时变放大器深度（0-127）.
        """
        command = [0xF0, 0x41, 0x00, 0x42, 0x12, 0x40, 0x20 | (channel & 0x0F), 0x00, high_pitch_volume & 0x7F, 0x00, 0xF7]
        self._write(command)
        for i, val in enumerate([time_varying_timbre_cutoff, amplitude, low_frequency_oscillator_rate, pitch_depth, time_varying_filter_depth, time_varying_amplifier_depth], 1):
            command[8], command[9] = i, val & 0x7F
            self._write(command)

    def all_drums(self):
        """在所有16个MIDI通道（0-15）上激活所有鼓通道并将所有16个MIDI通道（0-15）设置为鼓通道."""
        command = [0xF0, 0x41, 0x00, 0x42, 0x12, 0x40, 0x00, 0x15, 0x01, 0x00, 0xF7]
        for i in range(16):
            command[6] = 0x10 | (i & 0x0F)
            self._write(command)

