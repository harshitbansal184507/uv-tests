def main():
    print("Hello from sample-project!")

    import click
    import flask
    import httpx

    print("✅ all runtime imports ok")
    print(f"  click  {click.__version__}")
    print(f"  flask  {flask.__version__}")
    print(f"  httpx  {httpx.__version__}")


if __name__ == "__main__":
    main()