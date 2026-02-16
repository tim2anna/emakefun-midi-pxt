from micropython import const

# Reverberation effect type constants
# ==== 混响效果类型常量 ====

# Room reverberation type 1
# 房间混响类型1
MIDI_REVERBERATION_ROOM_1: int = const(0)

# Room reverberation type 2
# 房间混响类型2
MIDI_REVERBERATION_ROOM_2: int = const(1)

# Room reverberation type 3
# 房间混响类型3
MIDI_REVERBERATION_ROOM_3: int = const(2)

# Hall reverberation type 1
# 大厅混响类型1
MIDI_REVERBERATION_HALL_1: int = const(3)

# Hall reverberation type 2
# 大厅混响类型2
MIDI_REVERBERATION_HALL_2: int = const(4)

# Plate reverberation effect
# 板式混响效果
MIDI_REVERBERATION_PLATE: int = const(5)

# Delay reverberation effect
# 延迟混响效果
MIDI_REVERBERATION_DELAY: int = const(6)

# Panning delay reverberation effect
# 板式延迟混响效果
MIDI_REVERBERATION_PAN_DELAY: int = const(7)

# Chorus effect type constants
# ==== 合唱效果类型常量 ====

# Chorus effect type 1
# 合唱效果类型1
MIDI_CHORUS_1: int = const(0)

# Chorus effect type 2
# 合唱效果类型2
MIDI_CHORUS_2: int = const(1)

# Chorus effect type 3
# 合唱效果类型3
MIDI_CHORUS_3: int = const(2)

# Chorus effect type 4
# 合唱效果类型4
MIDI_CHORUS_4: int = const(3)

# Feedback chorus effect
# 反馈合唱效果
MIDI_CHORUS_FEEDBACK: int = const(4)

# Flanger-style chorus effect
# 颤音合唱效果
MIDI_CHORUS_FLANGER: int = const(5)

# Short delay chorus effect
# 短延迟合唱效果
MIDI_CHORUS_SHORT_DELAY: int = const(6)

# Feedback delay chorus effect
# 反馈延迟合唱效果
MIDI_CHORUS_FEEDBACK_DELAY: int = const(7)
