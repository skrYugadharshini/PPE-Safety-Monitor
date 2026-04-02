from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")  # change path if needed

# Run prediction
results = model.predict(
    source="image.jpg",   # change to your image
    save=True,
    conf=0.4
)

# SAFE / UNSAFE logic
for i, r in enumerate(results):
    labels = [model.names[int(cls)] for cls in r.boxes.cls]

    print(f"\nImage {i+1}")
    print("Detected labels:", labels)

    if "person" not in labels:
        print("Safety Status: No worker detected")
        continue

    has_helmet = "helmet" in labels
    has_vest = "vest" in labels
    has_no_helmet = "no-helmet" in labels
    has_no_vest = "no-vest" in labels

    if has_helmet and has_vest and not has_no_helmet and not has_no_vest:
        print("Safety Status: SAFE ✅")
    else:
        print("Safety Status: UNSAFE ❌")

        if has_no_helmet or not has_helmet:
            print("- Helmet violation")

        if has_no_vest or not has_vest:
            print("- Vest violation")