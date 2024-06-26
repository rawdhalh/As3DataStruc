import heapq  # Importing the heapq module for the MaxHeap data structure

class SocialMediaPosts:
    def __init__(self):
        self.posts = {}  # Initialize an empty dictionary to store social media posts

    def add_post(self, datetime, post, person):
        # Add a post to the social media posts dictionary
        self.posts[datetime] = (post, person)

    def find_post_by_datetime(self, datetime):
        # Find a post in the social media posts dictionary by its unique datetime
        return self.posts.get(datetime, None)

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.values = [value]
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None  # Initialize an empty root node for the Binary Search Tree

    def insert(self, key, value):
        # Insert a key-value pair into the Binary Search Tree
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        # Private method to recursively insert a key-value pair into the Binary Search Tree
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.values.append(value)
        return node

    def search_range(self, start_datetime, end_datetime):
        # Search for key-value pairs within a specific time range in the Binary Search Tree
        results = []  # Initialize an empty list to store search results
        self._search_range(self.root, start_datetime, end_datetime, results)
        return results

    def _search_range(self, node, start_datetime, end_datetime, results):
        # Private method to recursively search for key-value pairs within a time range
        if node is None:
            return
        if start_datetime <= node.key <= end_datetime:
            for value in node.values:
                results.append((node.key, value))
        if start_datetime < node.key:
            self._search_range(node.left, start_datetime, end_datetime, results)
        if end_datetime > node.key:
            self._search_range(node.right, start_datetime, end_datetime, results)

class MaxHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty list to store elements in the MaxHeap

    def add_post(self, views, post, person):
        # Add a post to the MaxHeap with its number of views as the priority
        heapq.heappush(self.heap, (-views, (post, person)))

    def get_most_viewed_post(self):
        # Get the post with the most views from the top of the MaxHeap
        if self.heap:
            return self.heap[0][1]
        else:
            return None

def main():
    social_media = SocialMediaPosts()  # Create an instance of the SocialMediaPosts class
    bst = BST()  # Create an instance of the Binary Search Tree class
    max_heap = MaxHeap()  # Create an instance of the MaxHeap class

    # Test cases for social media posts
    social_media.add_post("2024-04-26 10:00:00", "Hello", "@Salama123")
    social_media.add_post("2023-03-12 12:30:00", "At the beach!", "@Khaled234")
    social_media.add_post("2024-04-26 12:00:00", "today is a good day.", "@Reem_2002")
    social_media.add_post("2024-02-20 9:30:00", "Hi", "@Salem89")
    social_media.add_post("2024-04-26 7:29:21", "Hello", "@Salam123")
    social_media.add_post("2023-12-31 10:00:00", "Happy New Year", "@Shamsa_221")
    social_media.add_post("2023-01-26 10:00:00", "its so sunny", "@Zayed234")

    # Populate the Binary Search Tree and the MaxHeap with test case data
    for datetime in social_media.posts.keys():
        bst.insert(datetime, social_media.posts[datetime])
        views = len(social_media.posts[datetime][0])  # Number of characters in post is used as views for simplicity
        max_heap.add_post(views, social_media.posts[datetime][0], social_media.posts[datetime][1])

    # Creating a Menu foe the user to select their choice
    while True:
        print("\nMenu: Please select from 1-4 ")
        print("1. Find a post by its unique datetime value")
        print("2. Find posts in a specific time range")
        print("3. Prioritize social media posts by number of views")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            datetime = input("Enter datetime to find post (YYYY-MM-DD HH:MM:SS): ")
            post_info = social_media.find_post_by_datetime(datetime)
            if post_info:
                print("Found post:", post_info)
            else:
                print("No post found for given datetime.")
        elif choice == '2':
            start_datetime = input("Enter start datetime (YYYY-MM-DD HH:MM:SS): ")
            end_datetime = input("Enter end datetime (YYYY-MM-DD HH:MM:SS): ")
            posts_in_range = bst.search_range(start_datetime, end_datetime)
            print("Posts between {} and {}: {}".format(start_datetime, end_datetime, posts_in_range))
        elif choice == '3':
            most_viewed_post = max_heap.get_most_viewed_post()
            if most_viewed_post:
                print("Most viewed post:", most_viewed_post)
            else:
                print("No posts available.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

