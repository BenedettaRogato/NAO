import random

#Move Wrapper Class
class NaoMove:
    def __init__(self, name, duration,  preconditions, postconditions):
        self.name = name
        self.t = duration
        self.pre = preconditions
        self.post = postconditions


possible_moves = [   NaoMove('StandUp', 8.35,  False, True),
            NaoMove('AirGuitar', 4.10,   True,  False),
            NaoMove('ArmDance', 10.42, True,  True),
            NaoMove('BlowKisses', 4.58,  True,  True),
            NaoMove('Bow', 3.86, True,  True),
            NaoMove('DiagonalRight', 2.56, True, True),
            NaoMove('DanceMove', 6.13, True, True),
            NaoMove('SprinklerL', 4.14,   True,  True),
            NaoMove('SprinklerR', 4.36,  True,  True),
            #NaoMove('RightArm', 9.19,  None, None),
            NaoMove('TheRobot', 6.10,   True,  True),
            NaoMove('ComeOn', 3.62,   True,  True),
            NaoMove('StayingAlive', 5.90,   True,  True),
            NaoMove('Rhythm', 2.95,  True,  True),
            NaoMove('PulpFiction', 5.8,   True,  True),
            NaoMove('Wave', 3.72,  True,  True),
            NaoMove('Glory', 3.28,  True, True),
            NaoMove('Clap', 4.10,  True, True),
            NaoMove('Joy', 4.50,  True, True)]

poss_modified = possible_moves

list_fast_moves = ['I_StandInit', 'M_StandZero', 'M_Stand', 'Rhythm', 'DiagonalRight', 'F_Crouch']
list_normal_moves = ['ComeOn','Wave','Glory', 'M_SitRelax', 'M_Hello', 'M_WipeForehead','AirGuitar', 'BlowKisses', 'Bow', 'SprinklerL', 'SprinklerR', 'Clap', 'Joy' ]
list_slow_moves = ['ArmDance','StandUp', 'DanceMove', 'TheRobot','StayingAlive', 'PulpFiction', 'M_Sit']

#Compulsory Moves
mandatory = [NaoMove('I_StandInit', 1.60, True, True),
             NaoMove('M_WipeForehead', 4.48, True, True),
             NaoMove('M_Stand', 2.32, True, True),
             NaoMove('M_Hello', 4.34, True, True),
             NaoMove('M_Sit', 9.84, True, False),
             NaoMove('M_SitRelax', 3.92, True, False),
             NaoMove('M_StandZero',1.4, True, True),
             NaoMove('F_Crouch', 1.32, True, False)]

mandatory_modified = mandatory



# algorithm that finds the subsequence of moves, choosing the ones that respect the constraints
def generate_transition(past_moves,tot_time, analyzed_song):

    # in case the total time exceeds 170, no new subsequence will be generated -> the next moves will only be
    # mandatory ones
    if tot_time >= 170:
        return []
    # if the last move performed is crouch, no further subsequences will be generated
    if past_moves[-1].name == 'F_Crouch':
        return []

    else:
        # shuffle the list of possible moves
        random.shuffle(poss_modified)
        sequence = []
        count = 0
        val_tot= 0
        sequence_time = 0
        # if the post condition of the previous move is True (it means NAO is standing)
        if past_moves[-1].post:
            for i in poss_modified:
                # set of constraints (technical and style) that a move has to comply with:
                # 1) technical: pre condition of the move must be True (standing)
                # 2) technical: the sequence is composed of maximum 4 elements
                # 3) style: the move should not be in the last 4 -> prevent a repetitive movement
                # 4) style: the move can be used maximum 4 times in the entire choreography
                # 5) technical: constraint: the maximum time spent for a sequence cannot exceed 30 seconds
                # 6) technical: the move must belong to the right set (slow moves, normal moves or fast moves) according to the intensity

                if i.pre and count <= 4 and i not in past_moves[:-5:-1] and past_moves.count(
                        i) <= 4 and (sequence_time + i.t) <= 30:
                    round_time = int(round(tot_time + i.t))
                    intensity= analyzed_song[round_time]

                    val_move = value_BC(i.name, intensity)
                    val_tot += val_move
                    # towards the end of the iteration through mandatory moves, it can happen that the time left
                    # is not enough, and the sequence could be too long and exeed max time ,
                    # this check prevents this and exits the sequence generation early
                    if end_sequence(tot_time, sequence_time):
                        return sequence, val_tot
                    sequence, sequence_time, count = add_move_to_sequence(sequence, sequence_time, count, i)
                    # style additional constraint: if the last move performed is one pf the static mandatory
                    # submoves, such as rotation_handgun of opening_arms (which are poor style wise), then the next
                    # move cannot be another static mandatory moves, in order to give more fluidity to the movements



        # if post condition is False (NAO is sitting)
        else:
            for i in poss_modified:
                intensity = int(round(tot_time + i.t))
                val_move = value_BC(i.name, intensity)
                val_tot += val_move
                # similar constraints to the standing case
                if not i.pre and count <= 2 and i not in past_moves[:-5:-1] and past_moves.count(
                        i) <= 2 and sequence_time + i.t < 30:

                    if end_sequence(tot_time, sequence_time):
                        return sequence, val_tot

                    sequence, sequence_time, count = add_move_to_sequence(sequence, sequence_time, count, i)

        return sequence, val_tot
def value_BC(move, intensity):
    val_move = 0
    if (move in list_fast_moves and intensity >= 50) or (
            move in list_normal_moves and (intensity >= 40 and intensity < 50)) or (
            move in list_slow_moves and intensity < 40):
        if (move in list_fast_moves and intensity > 50):
            val_move = 1.0
        else:
            val_move = 0.9
    elif (move in list_fast_moves and (intensity >= 40 and intensity < 50)) or (
            move in list_normal_moves and (intensity < 40 or intensity >= 50) or (
            move in list_slow_moves and (intensity >= 40 and intensity < 50))):
        val_move = 0.3
    elif (move in list_fast_moves and intensity < 40) or (move in list_slow_moves and intensity >= 50):
        val_move = 0.1
    else:
        print("##########Error##################")
    return val_move


def end_sequence(tot_time, sequence_time):
    if (tot_time + sequence_time) >= 170:
        return True


def add_move_to_sequence(sequence, sequence_time, count, i):
    sequence.append(i)
    sequence_time += i.t
    count += 1
    return sequence, sequence_time, count