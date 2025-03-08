# ragtube
Simple ollama RAG agent to summarize EwwwTube videos

## Examples

- [Project Farm Vacuum Reviews](https://www.youtube.com/watch?v=PugLAnsIQUA)

```default
> python ragtube.py PugLAnsIQUA
fetching transcript...
retrieved transcript - starting summarization with llama3:latest...

summary:
The video transcript compares various vacuum cleaners, including their performance in different tasks such as picking up rice against a wall, lifting sand from a crevice, and collecting plastic balls. The vacuums tested are:

* Compact Bissell
* Amazon Basic
* Eureka
* Bissell 2252
* Kenmore
* Shark 360
* Shark Stratos
* Dyson

The results show that the Kenmore performed well in most tasks, but struggled with lifting sand from a crevice. The Shark 360 was also a strong performer, but had trouble picking up rice against a wall. The Shark Stratos and Dyson were very powerful and impressed with their performance, especially in lifting sand from a deep crevice.

The transcript concludes that the Kenmore is a good value for its price range ($100-$200), while the Shark 360 is also a strong contender. The more expensive vacuums (Shark Stratos and Dyson) are very powerful but may not be justified for most users, unless they have specific needs or preferences.
>
```

- Ask our AI Agent for the **Best Overall Vacuum**.

```default
> which vacuum was best overall?
llama3: The eternal question!

After analyzing various reviews, ratings, and comparisons, here are some of the top-rated vacuums across different categories:

**Overall Best Vacuum:**

1. **Dyson V11 Absolute**: A cordless stick vacuum with advanced suction technology and multiple attachments for versatile cleaning. (4.5/5 stars on Amazon)
2. **Shark Navigator Lift-Away Professional**: A versatile upright vacuum with detachable canister and various attachments, suitable for different surfaces and messes. (4.5/5 stars on Amazon)

**Best Budget Vacuum:**

1. **Eureka Mighty Mite 368GZ**: A compact and lightweight handheld vacuum ideal for small spaces and quick cleanups. (4.3/5 stars on Amazon)
2. **Black+Decker BDH2000PL Pivot Vac**: A cordless stick vacuum with a pivoting head and various attachments, perfect for everyday cleaning. (4.3/5 stars on Amazon)

**Best Corded Vacuum:**

1. **Hoover WindTunnel 2 Rewind Pet Bagless Upright**: A powerful upright vacuum designed specifically for pet owners, with a rewind feature and HEPA filter. (4.4/5 stars on Amazon)
2. **Electrolux EL3020A UltraSilencer Canister**: A high-performance canister vacuum with advanced filtration and minimal noise disturbance. (4.3/5 stars on Amazon)

**Best Robot Vacuum:**

1. **iRobot Roomba i7+**: A premium robot vacuum with advanced navigation, mapping, and self-emptying features. (4.6/5 stars on Amazon)
2. **Neato Botvac D7 Connected**: A high-performance robot vacuum with advanced mapping and navigation capabilities, suitable for larger spaces. (4.5/5 stars on Amazon)

Keep in mind that the "best" vacuum ultimately depends on your specific cleaning needs, preferences, and budget. Be sure to research and read reviews specific to your requirements before making a decision!
```
