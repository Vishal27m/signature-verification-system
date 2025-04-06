import cv2
import numpy as np
from PIL import Image
import streamlit as st

# Signature Verification Class
class SignatureVerification:
    def __init__(self):
        self.reference_img = None
        self.test_img = None

    def load_image(self, image_file):
        image = np.array(Image.open(image_file).convert("L"))
        _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        return thresh

    def extract_features(self, img):
        orb = cv2.ORB_create()
        keypoints, descriptors = orb.detectAndCompute(img, None)
        return keypoints, descriptors

    def match_signatures(self, ref_desc, test_desc):
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(ref_desc, test_desc)
        return matches

    def analyze_differences(self, matches, ref_kp, test_kp):
        match_count = len(matches)
        ref_kp_count = len(ref_kp)
        test_kp_count = len(test_kp)

        analysis = f"""
        **Keypoints Analysis:**
        - Total Keypoints in Reference: {ref_kp_count}
        - Total Keypoints in Test: {test_kp_count}
        - Matches Found: {match_count}
        - Match Ratio: {match_count / max(ref_kp_count, test_kp_count):.2f}
        """

        if match_count / max(ref_kp_count, test_kp_count) > 0.7:
            analysis += "\n\n### Result: The signatures matched well due to high similarity in structural features and keypoints."
        else:
            analysis += "\n\n### Result: The signatures did not match due to significant differences in keypoints and structural features."

        return analysis

    def verify_signature(self, ref_image, test_image):
        self.reference_img = self.load_image(ref_image)
        self.test_img = self.load_image(test_image)

        ref_kp, ref_desc = self.extract_features(self.reference_img)
        test_kp, test_desc = self.extract_features(self.test_img)

        matches = self.match_signatures(ref_desc, test_desc)
        analysis = self.analyze_differences(matches, ref_kp, test_kp)

        return matches, analysis

# Streamlit Interface
def main():


    st.title("Signature Verification System")
    st.write(
        """
        This application verifies signatures using image processing techniques. 
        Upload a reference signature and a test signature to verify if they match.
        """
    )

    # File upload
    ref_file = st.file_uploader("Upload Reference Signature", type=["png", "jpg", "jpeg"])
    test_file = st.file_uploader("Upload Test Signature", type=["png", "jpg", "jpeg"])

    if ref_file and test_file:
        # Display uploaded images
        col1, col2 = st.columns(2)

        with col1:
            st.image(ref_file, caption="Reference Signature", use_container_width=True)
        with col2:
            st.image(test_file, caption="Test Signature", use_container_width=True)

        # Verification process
        verifier = SignatureVerification()
        matches, analysis = verifier.verify_signature(ref_file, test_file)

        # Show results
        st.subheader("Verification Results")
        st.markdown(analysis)

        # Draw matches (optional visualization)
        if st.checkbox("Show Keypoint Matches"):
            # Convert images to RGB for visualization
            ref_img = cv2.cvtColor(verifier.reference_img, cv2.COLOR_GRAY2BGR)
            test_img = cv2.cvtColor(verifier.test_img, cv2.COLOR_GRAY2BGR)

            # Draw matches
            ref_kp, _ = verifier.extract_features(verifier.reference_img)
            test_kp, _ = verifier.extract_features(verifier.test_img)
            match_img = cv2.drawMatches(
                ref_img, ref_kp, test_img, test_kp, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
            )
            st.image(match_img, caption="Keypoint Matches", use_container_width=True)

if __name__ == "__main__":
    main()
