#!/usr/bin/env python3
"""
Custom Outreach Pitch Generator
Generates personalized SMS and email pitches for local contractor leads.
"""

import sys
import argparse

def generate_pitch(name: str, city: str, service: str, checkout_url: str = "https://whop.com/checkout/peaksaidevelopment") -> dict:
    sms = (
        f"Hey {name}, tried calling your shop just now regarding a {service} quote in {city}, "
        f"but got your voicemail. Most homeowners hang up and call the next guy on Google.\n\n"
        f"We install an automated text-back on your number for a flat $97 that texts missed callers "
        f"an instant booking link in 5 seconds so you keep the $400 job.\n\n"
        f"I can hook it up for your phone today. Checkout link here: {checkout_url}"
    )
    
    email_subject = f"Quick question about missed {service} calls in {city}"
    email_body = (
        f"Hi {name},\n\n"
        f"When a homeowner calls your phone while you're on a job site or driving, what happens?\n\n"
        f"In our testing with {service} contractors in {city}, 82% of callers hang up and call another contractor instead of leaving a voicemail.\n\n"
        f"We set up a simple missed-call auto-text: whenever you miss a call, the customer immediately receives an SMS with your quote and booking link.\n\n"
        f"We offer a 1-day setup for a flat $97 (pays for itself on the very first saved job).\n\n"
        f"Would you like me to set this up on your number this week?\n\n"
        f"Best,\nCalin | Peaks AI"
    )
    
    return {
        "sms": sms,
        "email_subject": email_subject,
        "email_body": email_body
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate personalized contractor pitches")
    parser.add_argument("--name", default="Business Owner", help="Contractor or business name")
    parser.add_argument("--city", default="Colorado Springs", help="City location")
    parser.add_argument("--service", default="exterior cleaning", help="Service type")
    parser.add_argument("--url", default="https://whop.com/checkout/peaksaidevelopment", help="Whop checkout link")
    
    args = parser.parse_args()
    pitch = generate_pitch(args.name, args.city, args.service, args.url)
    
    print("\n" + "="*50)
    print("PERSONALIZED SMS PITCH (Copy & Send):")
    print("="*50)
    print(pitch["sms"])
    print("\n" + "="*50)
    print("EMAIL PITCH:")
    print(f"Subject: {pitch['email_subject']}")
    print("="*50)
    print(pitch["email_body"])
    print("="*50 + "\n")
