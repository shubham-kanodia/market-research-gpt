# Problem

The problem is that there are images on the internet that are AI-generated or manipulated, and it is becoming increasingly difficult for individuals to determine whether an image is genuine or not. This can lead to misinformation, privacy concerns, and copyright infringements. A solution needs to be developed to help people distinguish between genuine and AI-generated images.

# Possible Solutions

The proposed protocol aims to tackle this problem by:

1. Attested camera sensor: Using a cryptographically signed camera sensor to prove that an image was taken from an actual camera and not algorithmically generated.
2. Tracking image edits: Storing information about every edit made to an image in the metadata to allow users to verify the authenticity of the image and the modifications made to it.

# Competitors

- Crypt (Cryptographic Image Signing): Oracle Cloud Infrastructure Registry offers a secure way to push and sign images using a master encryption key.

- CodeSign Secure: A secure and flexible solution for organizations to manage and protect their code signing processes.

- Sigstore project: An open-source initiative focused on storing and verifying cryptographic signatures, with a specific tool called Cosign for signing and verifying software packages.

# Existing technologies and standards

- EXIF data: A standard for storing digital photography information in image files. Websites like EXIFdata.com, Pic2Map, and Brandfolder offer tools to explore, extract, and view metadata.

- Convolutional Neural Networks (CNN): Research studies have used custom CNN architectures to detect fake images with a decent detection accuracy.

- Physics-based image forgery detection: Techniques like chromatic aberration, color filter arrays, source camera abbreviation, and sensor imperfection, among others, are used to detect image forgery.

# Use-cases

- Facial recognition systems: Enhancing the accuracy and security of facial recognition systems by verifying input images as genuine.

- Online media credibility: Preventing the spread of misinformation by ensuring that images used in news articles and social media platforms are authentic.

- Intellectual Property protection: Copyright owners can ensure that their content remains original and unaltered by tracking image edits and verifying the authenticity of images.

# Trends

- Increasing number of research studies on image forgery detection methods.
- Growing applications of AI-generated content, leading to a need for verification techniques.
- The emergence of open-source tools like Sigstore for cryptographic signature storage and verification.

# Conclusion

There is a need for a protocol that can help users verify the authenticity of an image, determine if it is genuine or AI-generated, and track any edits made to it. The proposed solution of using attested camera sensors and tracking image edits in the metadata shows promise. There is a