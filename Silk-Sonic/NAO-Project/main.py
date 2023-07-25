import os
from search import generate_transition, poss_modified, mandatory_modified
import music_detection as md
import subprocess
import multiprocessing
import sys
import glob, os


def playSong(song):
    if sys.platform.startswith('linux'):
        os.chdir('..')
        bashCommand = "play " + song
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    else:
        import winsound
        os.chdir('..')
        song = os.path.join(os.getcwd(), song)
        winsound.PlaySound(song, winsound.SND_FILENAME)

def do_move(curr_move, ip, port, tot_time, past_moves):
    python2_command = f"python2 -m {curr_move.name} {ip} {port}"
    process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
    print("Move: {}".format(curr_move.name), flush=True)
    past_moves.append(curr_move)
    tot_time += curr_move.t
    print("tempo realmente trascorso: ", tot_time)
    return tot_time,past_moves



def dance(mandatory_modified, analyzed_song, robot_ip, robot_port):
    tot_time = 0
    past_moves= []
    os.chdir('..')
    os.chdir('..')
    os.chdir(os.path.join(os.getcwd(), "moves"))

    tot_time, past_moves = do_move(mandatory_modified[0], robot_ip, robot_port, tot_time,past_moves)

    # starting iteration trough mandatory positions
    for i in range(1, len(mandatory_modified)):

        # creating a subsequence
        val_max = 0
        subsequence_final = []
        for k in range(0, 4):
            subsequence, val = generate_transition(past_moves,tot_time, analyzed_song )

            if val_max < val:
                val_max = val
                subsequence_final = subsequence


        for j in subsequence_final:
            # for each move (not including the first one) a check on its state will be performed, in
            # order to understand if NAO is sitting or standing
            tot_time, past_moves= do_move(j,robot_ip,robot_port,tot_time,past_moves)

        tot_time, past_moves = do_move(mandatory_modified[i], robot_ip,robot_port,tot_time,past_moves)

    # mixer.music.stop()

    s = 0
    for i in past_moves:
        s += i.t
    print
    'total time: ', s

def main():
    robot_ip = input("IP: ")
    robot_port = input("Port: ")

    list_songs = []
    os.chdir(os.getcwd() + "/Music")
    print()
    print("AVAILABLE SONGS:")
    i = 1
    for file in glob.glob("*.wav"):
        list_songs.append(file)
        print(i, ":", file)
        i += 1

    print()
    index = int(input("Which song would you like to play? Choose the number: "))
    sys.stdin.flush()
    print()
    song = list_songs[index - 1]
    print("You chose the song || " + song + " || let's dance nao!")

    print("AVAILABLE MANDATORY POSITIONS: ")
    i = 1
    for pos in mandatory_modified:
        print(i, ":", pos.name)
        i += 1

    numbers = input("Choose the mandatory position you want to remove (integer): ")
    numb = numbers.split()

    for str in numb:
        mandatory_modified.remove(mandatory_modified[int(str)-1])

    print()
    i = 0
    print("AVAILABLE OPTIONAL POSITIONS: ")

    for pos in poss_modified:
        print(i, ":", pos.name)
        i += 1

    numbers = input("Choose the optional position you want to remove (integer): ")
    print()
    numb = numbers.split()

    for str in numb:
        poss_modified.remove(poss_modified[int(str)])

    # --------------------------------------------------------------# ADDED
    # Select a random song and analyze the amplitude

    analyzed_song = md.analyze_music(song)
    # --------------------------------------------------------------# ADDED
    process1 = multiprocessing.Process(target=playSong, args=(song,))
    process2 = multiprocessing.Process(target=dance, args=(mandatory_modified, analyzed_song, robot_ip, robot_port))
    process1.start()
    process2.start()
    #process1.join()
    process2.join()
    process1.terminate()



if __name__ == '__main__':
    main()