from scamshield.core.model import train_model
from scamshield.core.pipeline import analyze_message

# Train model
model = train_model("data/sms.csv")

# Test message
message = "Microsoft support: your device is infected. Call immediately."

result = analyze_message(model, message)

print(result)