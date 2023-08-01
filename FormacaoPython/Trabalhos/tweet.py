
T = input()

def verificar_tweet(T):
    if len(T) <= 140 and len(T) >= 1:
        return "TWEET"
    else:
        return "MUTE" 
    
resultado = verificar_tweet(T)
print(resultado)
