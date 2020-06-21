import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path
import os, sys

def query_yes_no(question):
    valid = {"yes": 1, "y": 1, "ye": 1,
             "no": 0, "n": 0, "q": -1}

    prompt = "[Y/n/q] "

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if choice == '':
            return valid["y"]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'y' or 'n' or 'q').\n")

user='stavros'

basepath = Path(os.getcwd()) / f'{user}'
if not os.path.exists(basepath):
    os.makedirs(basepath)

prompts = []
prompts.append(['Καλημέρα σας', 'goodmorning'])
prompts.append(['Πώς μπορώ να σας εξυπηρετήσω;','howtoserve'])
prompts.append(['Θα ήθελα να ρωτήσω για την παραγγελία μου','askformyorder'])
prompts.append(['Ακόμα περιμένω να με ενημερώσετε','stillwaiting'])
prompts.append(['Πότε θα παραδοθεί η παραγγελία μου;','orderdelivery'])
prompts.append(['Δεν σας ακούω καθαρά','cannothear'])
prompts.append(['Παρακαλώ μιλήστε πιο δυνατά','talklouder'])
prompts.append(['Ευχαριστούμε που επικοινωνήσατε μαζί μας','thanksforcalling'])
prompts.append(['Το προϊόν είναι σε εγγύηση;','inwarranty'])
prompts.append(['Μπορείτε να μου πείτε πότε το αγοράσατε;','whenbought'])
prompts.append(['Από ποιο κατάστημα το αγοράσατε;','wherebought'])
prompts.append(['Δεν είμαι καθόλου ευχαριστημένος','nothappy'])
prompts.append(['Μετάνιωσα για την αγορά μου','regretit'])
prompts.append(['Χάλασε μετά από μία εβδομάδα','brokedown'])
prompts.append(['Δεν λειτουργεί σωστά','doesnotworkcorrectly'])
prompts.append(['Μου παραδώσατε λάθος μοντέλο','wrongmodel'])
prompts.append(['Ο πωλητής μου είπε ότι υπστηρίζει 4K','salesmantoldme4k'])
prompts.append(['Το αγόρασα στο κατάστημα στην Κηφισιά','boughtinkifisia'])
prompts.append(['Δεν θυμάμαι πότε το αγόρασα','dontrememberwhenbought'])
prompts.append(['Είχατε πει ότι θα παραδοθεί την Τρίτη','toldmedeliveryintuesday'])
prompts.append(['Καθυστέρησε η παράδοση από τον προμηθευτή','vendordelay'])
prompts.append(['Μπορώ να κλείσω ραντεβού για την Τρίτη πρωί;','scheduletuesdaymorning'])
prompts.append(['Θα ήθελα να κανονίσω ραντεβού για την Πέμπτη','schedulethursday'])
prompts.append(['Να έρθω την Παρασκευή','comeinfriday'])
prompts.append(['Είστε ανοικτά το Σάββατο','openinsaturday'])
prompts.append(['Δευτέρα το πρωί κατά τις 10 μπορείτε','monday10available'])
prompts.append(['Δεν μπορώ τόσο νωρίς, έχετε αργότερα;','cannotthattimelater'])
prompts.append(['Έχουμε διαθεσιμότητα την Τετάρτη το πρωί και την Παρασκευή το απόγευμα μετά τις 5, πότε σας βολεύει;','availablewednesdayandfriday'])
prompts.append(['Θα ήθελα να μιλήσω με τον υπεύθυνο','talkwithresponsible'])
prompts.append(['Δεν σας ακούω καλά, μπορείτε να μιλήσετε λίγο πιο δυνατά;','cannotheartalklouder'])
prompts.append(['Είμαστε κλειστά το Σάββατο, να το κανονίσουμε για τη Δευτέρα;','closedinsaturdayopenmonday'])
prompts.append(['Πρέπει να μιλήσατε με κάποιον συνάδελφο και δεν βλέπω να έχει σημειώσει το ραντεβού','talkwithothernoschedule'])
#100

#fs = 44100  # Sample rate
fs = 48000  # Sample rate

for prompt in prompts:

    seconds = len(prompt[0]) * 0.15 + 1 # Duration of recording

    while True:
        print(f'Please, say: "{prompt[0]}"')
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        user_input = query_yes_no("Continue to next sentence?")

        if user_input==1:
            break
        elif user_input==-1:
            exit()

    output_path = basepath / f"{prompt[1]}.wav"
    write(output_path, fs, myrecording)  # Save as WAV file
