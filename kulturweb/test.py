import arrow
import kultur


def main():
    kultur.init_database()
    kultur.get_shows(arrow.now(), arrow.now().shift(weeks=+1), "all", False)


if __name__ == "__main__":
    main()
