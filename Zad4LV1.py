x = int(input("Unesite prvi broj: "))
kvadrat = x * x
print(f"Rezultat je {kvadrat}.")  

def calculate_spam_confidence(filename):
    try:
        with open(filename, 'r') as file:
            total_confidence = 0
            count = 0
            
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    try:
                        confidence_value = float(line.split(':')[1].strip())
                        total_confidence += confidence_value
                        count += 1
                    except ValueError:
                        continue
            
            if count > 0:
                print(f"Average X-DSPAM-Confidence: {total_confidence / count}")
            else:
                print("No valid X-DSPAM-Confidence lines found.")
    except FileNotFoundError:
        print("File not found. Please check the filename.")
        
filename = input("Ime datoteke: ")
calculate_spam_confidence(filename)
