

def get_story_id():
    for i in range(1, 100):
        story_id = f'{str(i).zfill(3)}_'
        yield story_id


if __name__ == '__main__':
    pass
